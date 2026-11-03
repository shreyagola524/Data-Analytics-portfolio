import pandas as pd
import numpy as np

# ==========================================
# BLOCK 4: EMPLOYEE PROFILE SCRUBBING
# ==========================================
data_emp = {
    'Employee_ID': ['E01', 'E02', 'E03', 'E04'],
    'Full_Name': ['ALICE SMITH', 'bob johnson', 'Charlie Brown', 'DIANA PRINCE'],
    'Department': ['  HR  ', 'MARKETING', 'IT', 'SALES'],
    'Salary_USD': ['$90,000', '$85,000', '$120,000', '$95,000']
}
df_emp = pd.DataFrame(data_emp)

print("--- Employee Profile DataFrame ---")
df_emp['Full_Name'] = df_emp['Full_Name'].str.lower()
df_emp['Salary_USD'] = df_emp['Salary_USD'].str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip()
df_emp['Salary_USD'] = df_emp['Salary_USD'].astype(int)
df_emp['Department'] = df_emp['Department'].str.strip()
print(df_emp)

print("\n--- Q4: Filtering rows using .loc (Salary >= 95000) ---")
print(df_emp.loc[df_emp['Salary_USD'] >= 95000])

print("\n--- Q5: Extracting first 2 rows and first 3 columns using .iloc ---")
print(df_emp.iloc[0:2, 0:3])

print("\n--- Q6: Changing Bob's Department ---")
df_emp.loc[df_emp['Full_Name'] == 'bob johnson', 'Department'] = 'Digital Marketing'
print(df_emp)

# ==========================================
# BLOCK 6: PRODUCT INVENTORY CHECKS
# ==========================================
data_prod = {
    'Product_ID': [101, 102, 103, 104, 105, 106],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable', 'Headphones'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [1200, 25, 45, 300, 10, 80],
    'Stock': [15, 120, 85, 0, 250, 40]
}

df_prod = pd.DataFrame(data_prod)
print("\n--- Q1: Category = Accessories and Price > 20 ---")
print(df_prod[(df_prod['Category'] == "Accessories") & (df_prod['Price'] > 20)])

print("\n--- Q2: Stock > 5 (Name and Price columns) ---")
print(df_prod[df_prod['Stock'] > 5][['Product_Name', 'Price']])

print("\n--- Q3: Filter using .isin(['Electronics']) ---")
print(df_prod[df_prod['Category'].isin(['Electronics'])])

print("\n--- Q4: Mean Price ---")
print(df_prod['Price'].mean())

print("\n--- Q5: Category Value Counts ---")
print(df_prod['Category'].value_counts())

print("\n--- Q6: Total Stock by Category ---")
print(df_prod.groupby('Category')['Stock'].sum())

print("\n--- Q7: Min and Max Price by Category ---")
print(df_prod.groupby('Category').agg({'Price': ['min', 'max']}))

print("\n--- Q8: Names starting with 'K' or 'M' ---")
print(df_prod[df_prod['Product_Name'].str.startswith(('K','M'))])

print("\n--- Q9: Rename Column ---")
df_prod = df_prod.rename(columns={'Product_Name': 'Item_Name'})
print(df_prod.head())

print("\n--- Q10: First Row using .iloc[0] (or .loc[0]) ---")
print(df_prod.iloc[0])

print("\n--- Q11: Row subset 1:4 and column subset 1:3 ---")
print(df_prod.iloc[1:4, 1:3])

print("\n--- Q12: Accessories category with Item_Name and Stock ---")
print(df_prod.loc[df_prod['Category'] == 'Accessories', ['Item_Name', 'Stock']])
