def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


students = [
    ("Dharani", 95),
    ("Arun", 87),
    ("Priya", 76),
    ("Rahul", 64),
    ("Anu", 52),
    ("Kiran", 38)
]


print("----- STUDENT GRADE REPORT -----")

for name, marks in students:
    grade = calculate_grade(marks)
    print(f"{name:<10} Marks: {marks:<5} Grade: {grade}")