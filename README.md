Student Grade Calculator

📌 Project Overview

The Student Grade Calculator is a simple Python project that calculates a student's grade based on their marks.

The program uses predefined grading conditions with Python if, elif, and else statements. It can process multiple students and display their names, marks, and assigned grades.

🎯 Objective

The main objectives of this project are:

Practice Python conditional statements.

Understand how to work with student data.

Apply predefined marks ranges to assign grades.

Practice functions and loops in Python.

Handle invalid marks appropriately.

🛠️ Technologies Used

Python

Jupyter Notebook

VS Code

📊 Grading Criteria

Marks Range

Grade

90 – 100

A+

80 – 89

A

70 – 79

B

60 – 69

C

50 – 59

D

40 – 49

E

0 – 39

F

Below 0 or Above 100

Invalid

⚙️ How the Program Works

Store the student names and marks.

Pass each student's marks to the calculate_grade() function.

Check the marks against the predefined grading conditions.

Assign the appropriate grade.

Display the student's name, marks, and grade.

Program Flow

Student Data
     ↓
Read Student Marks
     ↓
Check Marks
     ↓
Assign Grade
     ↓
Display Result

💻 Example

Input

Dharani - 95
Arun - 87
Priya - 76
Rahul - 64
Anu - 52
Kiran - 38

Output

----- STUDENT GRADE REPORT -----
Dharani    Marks: 95    Grade: A+
Arun       Marks: 87    Grade: A
Priya      Marks: 76    Grade: B
Rahul      Marks: 64    Grade: C
Anu        Marks: 52    Grade: D
Kiran      Marks: 38    Grade: F

🧪 Testing

The program was tested with different marks to verify that the grading conditions work correctly.

Test Marks

Expected Grade

95

A+

87

A

76

B

64

C

52

D

45

E

38

F

105

Invalid

-5

Invalid

📁 Project Structure

Student-Grade-Calculator/
│
├── student_grade_calculator.py
├── Student_Grade_Calculator.ipynb
└── README.md

▶️ How to Run

Using Python

Open the project folder in VS Code.

Open the terminal.

Run:

python student_grade_calculator.py

Using Jupyter Notebook

Open Student_Grade_Calculator.ipynb.

Run the cells in order.

Check the displayed output.

📚 Concepts Learned

Variables

Input and output

Data types

if, elif, and else

Comparison operators

Functions

Lists and tuples

for loops

String formatting

Input validation

 Future Improvements

Allow users to enter an unlimited number of students.

Calculate class average marks.

Find the highest and lowest marks.

Count the number of students in each grade.

Generate graphical reports.

👨‍💻 Author

Dharani

This project was created as part of an AI & ML internship task.
## Streamlit Web Application

The Student Grade Calculator is also deployed as a web application using Streamlit.

Users can enter a student's name and marks, and the application calculates the corresponding grade.

### Live Demo

https://student-grade-calculator-ma47sayec4cquhj8uprdu.streamlit.app/

### Deployment

The application is deployed using Streamlit Community Cloud.

### Project Files

- `student_grade_calculator.py` - Main Python grade calculator
- `Student_Grade_Calculator.ipynb` - Jupyter Notebook implementation
- `app.py` - Streamlit web application
- `requirements.txt` - Python dependency for deployment
- `README.md` - Project documentation