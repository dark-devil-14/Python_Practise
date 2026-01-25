# Use a list to store marks for better scalability
subjects = ["DA 101", "DA 102", "DA 103", "DA 104"]
marks = [int(input(f"Enter marks for {sub}: ")) for sub in subjects]

total_marks = sum(marks) / len(marks)

# Check if the student passed all subjects first
if min(marks) > 35:
    if total_marks >= 90:
        grade = "A (Excellent)"
    elif total_marks >= 80:
        grade = "AB"
    elif total_marks >= 70:
        grade = "BB"
    elif total_marks >= 60:
        grade = "BC"
    elif total_marks >= 50:
        grade = "CC"
    elif total_marks >= 40:
        grade = "DD"
    else:
        grade = "F"
else:
    grade = "F (Failed in individual subject)"

print(f"Grade: {grade}")