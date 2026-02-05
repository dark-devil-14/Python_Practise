
#Happy year

year = (input())

def print_next_happy_year(year):
    for i in range(int(year)+1, 10000):
        year = str(i)
        new_check = (
        year[0] != year[1] and
        year[0] != year[2] and
        year[0] != year[3] and
        year[1] != year[2] and
        year[1] != year[3] and
        year[2] != year[3]
        )
        if(new_check):
            new_year = i
            print(new_year)
            break


check_1 = (
    year[0] != year[1] and
    year[0] != year[2] and
    year[0] != year[3] and
    year[1] != year[2] and
    year[1] != year[3] and
    year[2] != year[3]
)

print_next_happy_year(year)

