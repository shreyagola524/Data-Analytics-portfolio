import pandas as pd
import numpy as np

# ==========================================
# BLOCK 3: RAW SALES DATA CLEANING & REGIONAL AGGREGATION
# ==========================================
raw_sales_data = {
    "Transaction_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Customer_Name": [
        "ALICE SMITH", "BOB JONES", "charlie brown", "DAVID Miller",
        "BOB JONES", "eva green", "FRANK white", "ANNA black"
    ],
    "Age": [22, np.nan, 45, 34, np.nan, 19, 61, np.nan],
    "Product_Category": [
        "Tech-Gadgets", "Office-Supplies", "Tech-Gadgets", "Furniture-Home",
        "Office-Supplies", "Tech-Gadgets", "Furniture-Home", "Office-Supplies"
    ],
    "Revenue": ["$1200", "$450", np.nan, "$3100", "$450", "$850", "$4200", "$150"],
    "Cost": [800, 300, 0, 2000, 300, 600, 3000, 100]
}

df_sales = pd.DataFrame(raw_sales_data)
print("--- Raw Sales DataFrame ---")
print(df_sales)

print("\n--- Q1: Missing Values Count ---")
print(df_sales.isnull().sum())

print("\n--- Q2: Handling Duplicates (Drop Duplicates) ---")
df_sales = df_sales.drop_duplicates()
print(df_sales)

print("\n--- Q2: Fill Missing Numeric Data (Age with Median) ---")
df_sales["Age"] = df_sales["Age"].fillna(df_sales["Age"].median())
print(df_sales)

print("\n--- Q3: Stripping $ Symbol from Revenue ---")
print(df_sales["Revenue"].str.replace("$", " ", regex=False))

print("\n--- Q4: Filling Missing Values in Revenue ---")
print(df_sales["Revenue"].fillna("0"))

print("\n--- Q5: Missing Values Filter ---")
print(df_sales[df_sales['Revenue'].isnull()])
print(df_sales[df_sales['Age'].isnull()])

print("\n--- Q6: Title Customer Name ---")
df_sales["Customer_Name"] = df_sales["Customer_Name"].str.title()
print(df_sales["Customer_Name"])

# ==========================================
# BLOCK 5: REGIONAL REVENUE AGGREGATION
# ==========================================
raw_data_reg = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South', 'East', 'West'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Electronics', 'Furniture', 'Electronics'],
    'Revenue': [89, 67, 43, 99, 112, 34, 56, 29, 49, 52, 87, 17],
    'Quantity_Sold': [30, 12, 45, 8, 22, 28, 35, 15, 50, 38, 10, 42]
}
df_reg = pd.DataFrame(raw_data_reg)

print("\n--- Q1: Group by Region and Category (Mean/Sum) ---")
output1 = df_reg.groupby(['Region', 'Category']).agg({
    'Revenue': ['mean', 'sum'],
    'Quantity_Sold': ['sum', 'count']
})
print(output1)

print("\n--- Q2: FIXED (Combined metrics for Revenue to avoid overwriting) ---")
result = df_reg.groupby('Region').agg({
    'Revenue': ['mean', 'sum'],
    'Quantity_Sold': ['sum']
})
print(result)

print("\n--- Q3: FIXED ---")
output2 = df_reg.groupby(['Region', 'Category']).agg({
     'Revenue': ['mean', 'sum'],
     'Quantity_Sold': ['sum']
})
print(output2)

print("\n--- Q4: Calculating Total & Avg Revenue, Total Qty Sold by Region ---")
output3 = df_reg.groupby('Region').agg({
    'Revenue': ['mean', 'sum'],
    'Quantity_Sold': ['sum']
})
print(output3)
