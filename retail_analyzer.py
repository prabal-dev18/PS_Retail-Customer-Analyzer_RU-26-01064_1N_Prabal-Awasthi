import pandas as pd

try:
    df = pd.read_csv("customers.csv")
except FileNotFoundError:
    print("Error: customers.csv file not found.")
    exit()

print("\n===== RETAIL CUSTOMER ANALYZER =====")

print("\n1. Spending Statistics")

print("Mean Spending:", df["TotalSpent"].mean())
print("Median Spending:", df["TotalSpent"].median())
print("Highest Spending:", df["TotalSpent"].max())
print("Lowest Spending:", df["TotalSpent"].min())

highest = df.loc[df["TotalSpent"].idxmax()]
lowest = df.loc[df["TotalSpent"].idxmin()]

print("\nHighest Spending Customer:", highest["Name"])
print("Lowest Spending Customer:", lowest["Name"])
print("\n2. High-Value Customers")

try:
    limit = float(input("Enter minimum spending amount: "))

    if limit < 0:
        print("Error: Amount cannot be negative.")
    else:
        high_value = df[df["TotalSpent"] >= limit]
        print("\nHigh-Value Customers:")
        print(high_value)

except ValueError:
    print("Error: Please enter a valid number.")
print("\n3. City-wise Spending Summary")

city_summary = df.groupby("City")["TotalSpent"].agg(["sum", "mean"])

print(city_summary)
