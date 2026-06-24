import pandas as pd

try:
    # Kyunki tumhari file 'notebook' folder se ek kadam bahar rakhi hai
    df = pd.read_csv("../cleaned_sales_data.csv")
    print("✅ Data successfully load ho gaya hai!")
    
    print("\n--- Data ka Size (Rows, Columns) ---")
    print(df.shape)
    
    print("\n--- Data ke pehle 5 rows ---")
    print(df.head())
except FileNotFoundError:
    print("❌ Error: 'cleaned_sales_data.csv' file nahi mili!")