# Python-Data-Processing-Mini-Project-
A simple program which reads a CSV file of expenses and calculates basic spending statistics using pandas 

## Files Included
* `Data Processing Project.py` - Main Python script for cleaning and analyzing the data.
* `expenses.csv` - Dataset containing 30 expense records across different categories and payment methods.

## What the Code Does
* **Data Cleaning:** Removes duplicate entries, drops rows with missing amounts, fixes inconsistent capitalization in categories, and standardizes `Bank Transfer` entries to `UPI`.
* **Basic Statistics:** Calculates total spending, average (mean), median, and standard deviation.
* **Breakdowns:** Shows average spending per payment method, UPI-specific average, and transaction counts by payment method and category.

## How to Run
1. Make sure Python is installed on your system.
2. Install Pandas:
   ```bash
   pip install pandas
   ```
3. Run the script from the project folder:
   ```bash
   python "Data Processing Project.py"
   ```
