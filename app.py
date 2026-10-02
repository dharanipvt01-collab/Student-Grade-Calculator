import streamlit as st


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


st.title("🎓 Student Grade Calculator")

st.write("Enter the student's details to calculate the grade.")

name = st.text_input("Student Name")

marks = st.number_input(
    "Enter Marks",
    min_value=0.0,
    max_value=100.0,
    value=0.0
)

if st.button("Calculate Grade"):

    if name.strip() == "":
        st.warning("Please enter the student name.")

    else:
        grade = calculate_grade(marks)

        st.subheader("Student Result")

        st.write("**Student Name:**", name)
        st.write("**Marks:**", marks)
        st.write("**Grade:**", grade)

        if grade == "A+":
            st.success("Excellent! 🎉")
        elif grade == "A":
            st.success("Very Good! 👏")
        elif grade == "F":
            st.error("The student has failed.")
        else:
            st.info("Grade calculated successfully.")