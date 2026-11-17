import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def clean_data(f):
    f = f.drop_duplicates()
    f = f.dropna(subset=['Amount'])
    f['Category'] = f['Category'].str.strip().str.title()
    f['Payment_Method'] = f['Payment_Method'].replace('Bank Transfer', 'UPI')
    return f

def basic_stats(f):
    print("\n" + "=" * 35)
    print("         BASIC STATISTICS")
    print("=" * 35)
    print(f"{'Total Spent:':<22} {f['Amount'].sum():>10.2f}")
    print(f"{'Average Expense:':<22} {f['Amount'].mean():>10.2f}")
    print(f"{'Median Expense:':<22} {f['Amount'].median():>10.2f}")
    print(f"{'Standard Deviation:':<22} {f['Amount'].std():>10.2f}")

def payment_stats(f):
    print("\n" + "=" * 35)
    print("        PAYMENT METHOD STATS")
    print("=" * 35)
    
    print("Average by Method:")
    avg_method = f.groupby('Payment_Method')['Amount'].mean()
    for method, avg in avg_method.items():
        print(f"  - {method:<18} {avg:>10.2f}")

    upi_avg = f[f['Payment_Method'] == 'UPI']['Amount'].mean()
    print(f"\n{'UPI Average:':<22} {upi_avg:>10.2f}")

    print("\nPayment Frequency:")
    freq_method = f['Payment_Method'].value_counts()
    for method, count in freq_method.items():
        print(f"  - {method:<18} {count:>10}")

def category_stats(f):
    print("\n" + "=" * 35)
    print("         CATEGORY BREAKDOWN")
    print("=" * 35)
    print("Category Frequency:")
    freq_cat = f['Category'].value_counts()
    for cat, count in freq_cat.items():
        print(f"  - {cat:<18} {count:>10}")
    print("=" * 35 + "\n")

f = load_data("expenses.csv")
f = clean_data(f)

basic_stats(f)
payment_stats(f)
category_stats(f)
