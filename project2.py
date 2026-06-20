import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating ecommerce data

data = {
    "Order_ID": np.arange(101,111),
    "Product": [
        "Laptop","Mobile","Shoes","Watch","Laptop",
        "Headphone","Mobile","Shoes","Watch","Tablet"
    ],
    "Category": [
        "Electronics","Electronics","Fashion","Fashion",
        "Electronics","Electronics","Electronics",
        "Fashion","Fashion","Electronics"
    ],
    "Price": np.random.randint(1000,50000,10),
    "Quantity": np.random.randint(1,5,10),
    "Month": [
        "Jan","Jan","Feb","Feb","Mar",
        "Mar","Apr","Apr","May","May"
    ]
}


df = pd.DataFrame(data)

# Revenue calculation
df["Revenue"] = df["Price"] * df["Quantity"]


print("----- Ecommerce Data -----")
print(df)


# Total sales
total_sales = np.sum(df["Revenue"])
print("\nTotal Revenue:", total_sales)


# Best selling product
best_product = df.groupby("Product")["Quantity"].sum()

print("\nBest Selling Product:")
print(best_product.sort_values(ascending=False).head(1))


# Category wise revenue
category_sales = df.groupby("Category")["Revenue"].sum()

print("\nCategory Revenue:")
print(category_sales)


# Monthly sales
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)



# Graph 1 Product Revenue

plt.figure(figsize=(8,5))

plt.bar(df["Product"],df["Revenue"])

plt.xticks(rotation=45)

plt.title("Product Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.show()



# Graph 2 Category Sales

plt.figure(figsize=(6,4))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Category Wise Sales")

plt.show()



# Graph 3 Monthly Sales

plt.figure(figsize=(7,4))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()