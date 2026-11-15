# Python-Data-Processing-Mini-Project-
A simple program which reads a CSV file of expenses and calculates basic spending statistics using pandas 

## Files Included
* `Data Processing Project.py` - Main Python script for cleaning and analyzing the data.
* `expenses.csv` - Dataset containing 30 expense records across different categories and payment methods.

## How it Works 
* load_data(filename) reads the CSV 
* clean_data(f) removes duplicate entries, drops rows with missing amounts, fixes inconsistent capitalization in categories, and standardizes `Bank Transfer` entries to `UPI`
* basic_stats(f), payment_stats(f), category_stats(f) calcualte the statistics from the given CSV using functions from Pandas. 


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
## AI Usage in the code 
- AI generated the CSV which was used in the program 
 The generated dataset had 3 flaws. 
  1. 2 blank amounts (Row 7 and 28)
  2. 2 duplicate rows 
  3. Inconsistent Capitalization
  **I used an AI Assistant to help with parts of the code** 
