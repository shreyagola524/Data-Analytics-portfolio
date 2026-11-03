import pandas as pd
import numpy as np

# ==========================================
# BLOCK 1: STUDENT DATA
# ==========================================
df_students = pd.DataFrame({
    "Name": ["Aarav", "Priya", "Rahul", "Sneha", "Vikram", "Ananya", "Rohan", "Neha"],
    "Age": [21, 23, 20, 22, 24, 21, 25, 23],
    "City": ["Delhi", "Mumbai", "Lucknow", "Delhi", "Pune", "Jaipur", "Mumbai", "Lucknow"],
    "Course": ["Python", "Data Science", "Python", "Machine Learning", "Data Science", "Python", "Machine Learning", "Python"],
    "Marks": [85, 92, 78, 88, 95, 81, 89, 76],
    "Attendance": [90, 95, 82, 88, 96, 85, 91, 79]
})
print("--- Students DataFrame ---")
print(df_students)

print("\n--- Missing Values Check ---")
print(df_students.isnull())

# ==========================================
# BLOCK 2: EMPLOYEE & DEPARTMENT DATA
# ==========================================
employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105, 106],
    "name": ["Aman", "Priya", "Rahul", "Sneha", "Arjun", "Neha"],
    "dept_id": [1, 2, 1, 3, 2, 4],
    "salary": [50000, 60000, 55000, 70000, 65000, 48000]
})

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "department": ["IT", "HR", "Finance", "Marketing"],
    "location": ["Delhi", "Mumbai", "Pune", "Bangalore"]
})

print("\n--- Filter Salary > 60000 ---")
print(employees[employees['salary'] > 60000])

print("\n--- Name and Salary Columns ---")
print(employees[['name','salary']])

print("\n--- Inner Merge Results ---")
print(pd.merge(employees, departments, how='inner', on='dept_id'))

print("\n--- Multi-level Filtering (Salary > 60000 & Dept ID == 1) ---")
merged_df = pd.merge(employees, departments, how='inner', on='dept_id')
filtered_df = merged_df[(merged_df['salary'] > 60000) & (merged_df['dept_id'] == 1)]
print(filtered_df)

print("\n--- Average Salary ---")
print(employees['salary'].mean())

print("\n--- Total Salary by Dept ID ---")
print(employees.groupby('dept_id')['salary'].sum())

print("\n--- Row of Highest Salary Employee ---")
print(employees[employees['salary'] == employees['salary'].max()])

print("\n--- Location-based Filtering (Mumbai or Delhi) ---")
merged_df = pd.merge(employees, departments, how='inner', on='dept_id')
filtered_df = merged_df[(merged_df['location'] == 'Mumbai') | (merged_df['location'] == 'Delhi')]
print(filtered_df)
