import numpy as np
import pandas as pd

marks = np.array([72,85,91,68,77])

print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

data = {
    "Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul"],
    "Attendance": [88,92,76,95,81],
    "Marks": [72,85,68,91,77]
}

df = pd.DataFrame(data)

print("\n------First Five Records------")
print(df.head())

print("\n------Data Information------")
print(df.info())

print("\n------Statistical summary------")
print(df.describe())

print("\nAverage marks:", df["Marks"].mean())

internal_marks = np.array([78, 85, 67, 92, 74, 88, 81, 69, 95, 76])

print("\n----- Internal Marks of 10 Students -----")
print("Internal Marks:", internal_marks)

print("Mean:", np.mean(internal_marks))
print("Median:", np.median(internal_marks))
print("Standard Deviation:", np.std(internal_marks))
print("Maximum:", np.max(internal_marks))
print("Minimum:", np.min(internal_marks))

student_data = {
    "Student_Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul"],
    "Roll_Number": [101, 102, 103, 104, 105],
    "Marks": [72, 85, 68, 91, 77],
    "Attendance": [88, 92, 76, 95, 81]
}

student_df = pd.DataFrame(student_data)

print("\n------ Student Data ------")
print(student_df)

above_80 = student_df[student_df["Marks"] > 80]

print("\n----- Students Who Scored Above 80 Marks -----")
print(above_80)

conditions = [
    student_df["Marks"] >= 90,
    student_df["Marks"] >= 80,
    student_df["Marks"] >= 70,
    student_df["Marks"] >= 60,
    student_df["Marks"] < 60
]

grades = ["A", "B", "C", "D", "F"]

student_df["Grade"] = np.select(
    conditions,
    grades,
    default="F"
)

print("\n----- Student Data with Grades -----")
print(student_df)