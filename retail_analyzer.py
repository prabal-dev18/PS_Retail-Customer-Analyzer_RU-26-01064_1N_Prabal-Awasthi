import pandas as pd

try:
    df = pd.read_csv("customers.csv")
except FileNotFoundError:
    print("Error: customers.csv file not found.")
    exit()

print("\n===== RETAIL CUSTOMER ANALYZER =====")
print("\n1. Spending Statistics")
print("2. High-Value Customers")
print("3. City-wise Spending Summary")

choice = input("Enter your choice: ")

if choice == "1":

    print("\nMean Spending:", df["TotalSpent"].mean())
    print("Median Spending:", df["TotalSpent"].median())

    highest = df.loc[df["TotalSpent"].idxmax()]
    lowest = df.loc[df["TotalSpent"].idxmin()]

    print("Highest Spending Customer:", highest["Name"])
    print("Lowest Spending Customer:", lowest["Name"])

elif choice == "2":

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

elif choice == "3":

    city_summary = df.groupby("City")["TotalSpent"].agg(["sum", "mean"])
    print("\nCity-wise Spending Summary:")
    print(city_summary)

else:
    print("Invalid choice.")
