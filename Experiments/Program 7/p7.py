import pandas as pd

order_data = pd.DataFrame({
    "Customer ID": [101, 102, 101, 103, 102, 101],
    "Order Date": ["2024-01-10", "2024-01-12", "2024-01-15",
                   "2024-01-18", "2024-01-20", "2024-01-25"],
    "Product Name": ["Laptop", "Mouse", "Keyboard",
                     "Laptop", "Mouse", "Laptop"],
    "Order Quantity": [2, 5, 3, 1, 4, 2]
})

order_data["Order Date"] = pd.to_datetime(order_data["Order Date"])

orders_per_customer = order_data.groupby("Customer ID").size()

avg_quantity = order_data.groupby("Product Name")["Order Quantity"].mean()

earliest_date = order_data["Order Date"].min()
latest_date = order_data["Order Date"].max()

print("Total Orders by Each Customer:")
print(orders_per_customer)

print("\nAverage Order Quantity for Each Product:")
print(avg_quantity)

print("\nEarliest Order Date:", earliest_date.date())
print("Latest Order Date:", latest_date.date())