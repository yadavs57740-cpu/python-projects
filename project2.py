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


# Revenue

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



# -------- ALL CHARTS IN ONE FIGURE --------


plt.figure(figsize=(15,5))


# Chart 1 Product Revenue

plt.subplot(1,3,1)

plt.bar(
    df["Product"],
    df["Revenue"]
)

plt.xticks(rotation=45)

plt.title("Product Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")



# Chart 2 Category Sales

plt.subplot(1,3,2)

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Category Sales")



# Chart 3 Monthly Sales

plt.subplot(1,3,3)

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid()


# Adjust spacing

plt.tight_layout()


# Show all


plt.savefig("ecommerce_output.png", dpi=300, bbox_inches="tight")
plt.show()
