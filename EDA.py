import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Path Configuration ---
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "cleaned_sales_data.csv")
images_dir = os.path.join(script_dir, "..", "Images")

# 1. Data Load
try:
    df = pd.read_csv(csv_path, encoding='latin1')
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print(f"❌ Error: File nahi mili!")
    exit()

df.columns = [col.lower() for col in df.columns]

# Setting background style for charts
sns.set_theme(style="whitegrid")

# --- CHART 1: Sales by Region ---
if 'region' in df.columns and 'sales' in df.columns:
    plt.figure(figsize=(10, 6))
    region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)
    sns.barplot(x=region_sales.index, y=region_sales.values, palette="viridis")
    plt.title("Total Sales by Region", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "sales_by_region.png"))
    print("📊 Chart 1: 'sales_by_region.png' updated!")

# --- CHART 2: Profit by Product Category ---
if 'category' in df.columns and 'profit' in df.columns:
    plt.figure(figsize=(10, 6))
    cat_profit = df.groupby("category")["profit"].sum().sort_values(ascending=False)
    sns.barplot(x=cat_profit.index, y=cat_profit.values, palette="coolwarm")
    plt.title("Total Profit by Product Category", fontsize=14, fontweight='bold')
    plt.xlabel("Category")
    plt.ylabel("Total Profit")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "profit_by_category.png"))
    print("📊 Chart 2: 'profit_by_category.png' saved!")

# --- CHART 3: Monthly Sales Trend (Line Chart) ---
if 'month' in df.columns and 'sales' in df.columns:
    plt.figure(figsize=(10, 6))
    # Month wise sort karke sales ka sum nikala
    monthly_sales = df.groupby("month")["sales"].sum()
    
    # Line chart banane ke liye
    plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b', linewidth=2)
    plt.title("Monthly Sales Trend", fontsize=14, fontweight='bold')
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(range(1, 13)) # 1 se 12 mahine dikhane ke liye
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "monthly_sales_trend.png"))
    print("📊 Chart 3: 'monthly_sales_trend.png' saved!")

print("\n🚀 Sabhi charts ready hain! Ek baar Images folder check karo bhai.")