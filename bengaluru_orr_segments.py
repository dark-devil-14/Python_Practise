import argparse
import re

import geopandas as gpd
import osmnx as ox
import pandas as pd
from shapely.geometry import LineString
from shapely.ops import linemerge, substring, unary_union

ORR_PATTERN = re.compile(r"\bouter\s*ring\s*(road|rd)\b|\borr\b", re.IGNORECASE)


def _is_orr_name(value) -> bool:
    if value is None:
        return False
    values = value if isinstance(value, (list, tuple, set)) else [value]
    return any(ORR_PATTERN.search(str(v)) for v in values if v is not None)


def _to_single_linestring(geometry):
    if geometry.is_empty:
        raise ValueError("Merged geometry is empty")
    if geometry.geom_type == "LineString":
        return geometry

    lines = [g for g in getattr(geometry, "geoms", []) if g.geom_type == "LineString" and not g.is_empty]
    if not lines:
        raise ValueError("No valid LineString geometry found")
    if len(lines) == 1:
        return lines[0]

    current = max(lines, key=lambda l: l.length)
    coords = list(current.coords)
    remaining = [l for l in lines if l is not current]

    while remaining:
        end_x, end_y = coords[-1]
        best_idx = None
        best_reverse = False
        best_distance = float("inf")

        for idx, line in enumerate(remaining):
            start = line.coords[0]
            finish = line.coords[-1]
            d_start = ((end_x - start[0]) ** 2 + (end_y - start[1]) ** 2) ** 0.5
            d_finish = ((end_x - finish[0]) ** 2 + (end_y - finish[1]) ** 2) ** 0.5
            if d_start < best_distance:
                best_idx, best_reverse, best_distance = idx, False, d_start
            if d_finish < best_distance:
                best_idx, best_reverse, best_distance = idx, True, d_finish

        chosen = remaining.pop(best_idx)
        chosen_coords = list(chosen.coords)
        if best_reverse:
            chosen_coords.reverse()
        coords.extend(chosen_coords[1:])

    return LineString(coords)


def build_segments_dataframe(graphml_path: str, segment_length_m: float = 500.0) -> pd.DataFrame:
    graph = ox.load_graphml(graphml_path)
    edges = ox.graph_to_gdfs(graph, nodes=False, fill_edge_geometry=True)

    if "name" not in edges.columns:
        raise ValueError("Graph edges do not contain a 'name' column")

    orr_edges = edges[edges["name"].apply(_is_orr_name)].copy()
    if orr_edges.empty:
        raise ValueError("No edges matched Outer Ring Road")

    metric_crs = orr_edges.estimate_utm_crs()
    orr_edges = orr_edges.to_crs(metric_crs)

    merged = linemerge(unary_union(orr_edges.geometry.dropna().to_list()))
    merged_line = _to_single_linestring(merged)

    records = []
    total_length = merged_line.length
    idx = 1
    start = 0.0

    while start < total_length:
        end = min(start + segment_length_m, total_length)
        segment = substring(merged_line, start, end)
        if not segment.is_empty and segment.length > 0:
            records.append({"segment_id": idx, "geometry": segment.centroid, "length_m": segment.length})
            idx += 1
        start = end

    centroids = gpd.GeoDataFrame(records, geometry="geometry", crs=metric_crs).to_crs(epsg=4326)
    return pd.DataFrame(
        {
            "segment_id": centroids["segment_id"],
            "latitude": centroids.geometry.y,
            "longitude": centroids.geometry.x,
            "length_m": centroids["length_m"],
        }
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("graphml_path")
    parser.add_argument("output_csv")
    parser.add_argument("--segment-length", type=float, default=500.0)
    args = parser.parse_args()

    df = build_segments_dataframe(args.graphml_path, args.segment_length)
    df.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
