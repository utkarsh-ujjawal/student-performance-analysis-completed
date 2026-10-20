import pandas as pd

# Load student data
df = pd.read_csv("students.csv")

# Display all student records
print("\n===== STUDENT PERFORMANCE ANALYSIS =====")
print(df)

# Calculate average marks
subjects = ["Python", "Mathematics", "English"]
df["Average"] = df[subjects].mean(axis=1).round(2)

# Calculate total marks
df["Total"] = df[subjects].sum(axis=1)

# Display results
print("\n===== STUDENT RESULTS =====")
print(df[["Name", "Total", "Average", "Attendance"]])

# Find the topper
topper = df.loc[df["Average"].idxmax()]

print("\n===== CLASS TOPPER =====")
print("Name:", topper["Name"])
print("Average Marks:", topper["Average"])

# Calculate class average
print("\nClass Average:", round(df["Average"].mean(), 2))

# Save analyzed data
df.to_csv("analysis_results.csv", index=False)

print("\nAnalysis completed successfully!")
print("Results saved in analysis_results.csv")
import matplotlib.pyplot as plt

# Student-wise average marks graph
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Average"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("student_performance.png")
plt.show()
# Pass or Fail Analysis
df["Result"] = df[subjects].apply(
    lambda row: "Pass" if all(mark >= 40 for mark in row) else "Fail",
    axis=1
)

print("\n===== PASS / FAIL ANALYSIS =====")
print(df[["Name", "Python", "Mathematics", "English", "Result"]])

print("\nTotal Passed:", (df["Result"] == "Pass").sum())
print("Total Failed:", (df["Result"] == "Fail").sum())
# Attendance Analysis
print("\n===== ATTENDANCE ANALYSIS =====")

print(df[["Name", "Attendance"]])

average_attendance = df["Attendance"].mean()

print("\nAverage Attendance:", round(average_attendance, 2), "%")

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with Attendance Below 75%:")
print(low_attendance[["Name", "Attendance"]])
# Enhanced Analysis: Subject-wise Performance
print("\n===== SUBJECT-WISE PERFORMANCE =====")

subject_averages = df[subjects].mean().round(2)

for subject, average in subject_averages.items():
    print(f"{subject} Average: {average}")

# Enhanced Attendance Status
df["Attendance Status"] = df["Attendance"].apply(
    lambda attendance: "Low Attendance"
    if attendance < 75 else "Satisfactory Attendance"
)

print("\n===== ATTENDANCE STATUS =====")
print(df[["Name", "Attendance", "Attendance Status"]])

# Save enhanced results
df.to_csv("analysis_results.csv", index=False)
print("\nEnhanced results saved successfully!")

# Subject-wise comparison graph
plt.figure(figsize=(8, 5))
plt.bar(subject_averages.index, subject_averages.values)
plt.title("Subject-wise Class Average")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("subject_comparison.png")
plt.show()