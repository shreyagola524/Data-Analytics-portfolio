# Python Pandas Practice

This folder contains my daily practice scripts where I am learning how to use **Pandas** and **NumPy** to clean, manipulate, and analyze data. I am building these skills to support my transition into Data and Business Analytics.

## 📁 What's Inside This Folder?

*   **`employee_and_hr_analytics.py`**
    *   Creating dataframes from scratch.
    *   Joining different data tables together using `pd.merge()`.
    *   Filtering employee records using conditional logic (e.g., matching specific departments and salaries).
*   **`sales_and_revenue_cleaning.py`**
    *   Finding and counting missing data points using `.isnull().sum()`.
    *   Handling missing values (`NaN`) by replacing them with the column median.
    *   Cleaning messy string data by removing `$` symbols and formatting text using `.str.title()`.
    *   Grouping financial metrics using `.groupby()` and `.agg()` to calculate total and average revenue.
*   **`product_inventory_checks.py`**
    *   Filtering data records using specific keywords with `.isin()` and `.str.startswith()`.
    *   Slicing specific rows and columns out of a dataset using `.loc` and `.iloc`.
    *   Renaming columns and calculating basic inventory summaries like `.mean()`, `.sum()`, and `.value_counts()`.

## ⚙️ How to Run These Scripts
If you want to run these files on your local machine:
1. Make sure you have Python installed.
2. Install the required libraries: `pip install pandas numpy`
3. Run any script from your terminal or command prompt: 
   ```cmd
   python sales_and_revenue_cleaning.py
   ```

*This folder is part of my main Data Analytics Portfolio repository, showcasing my progression from data cleaning with Python to visualising insights in my dashboards.*

