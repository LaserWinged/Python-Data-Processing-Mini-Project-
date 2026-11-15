import pandas as pd

def load_data(filename):
    f = pd.read_csv(filename)
    return f

def clean_data(f):
    f = f.drop_duplicates()
    f = f.dropna(subset=['Amount'])
    f['Category'] = f['Category'].str.strip().str.title()
    f['Payment_Method'] = f['Payment_Method'].replace('Bank Transfer', 'UPI')
    return f

def basic_stats(f):
    print("Total:", f['Amount'].sum())
    print("Average:", f['Amount'].mean())
    print("Median:", f['Amount'].median())
    print("Standard Deviation:", f['Amount'].std())

def payment_stats(f):
    print("\nAverage by Method:\n", f.groupby('Payment_Method')['Amount'].mean())
    print("\nUPI Average:", f[f['Payment_Method'] == 'UPI']['Amount'].mean())
    print("\nPayment Frequency:\n", f['Payment_Method'].value_counts())

def category_stats(f):
    print("\nCategory Frequency:\n", f['Category'].value_counts())

f = load_data("expenses.csv")
f = clean_data(f)

basic_stats(f)
payment_stats(f)
category_stats(f)




