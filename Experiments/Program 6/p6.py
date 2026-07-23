prices = [50, 30, 20, 40]
quantities = [2, 3, 5, 1]

discount_rate = 5  
tax_rate = 5         

subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount = subtotal * discount_rate / 100

amount_after_discount = subtotal - discount

tax = amount_after_discount * tax_rate / 100

total_cost = amount_after_discount + tax

print("Subtotal =", subtotal)
print("Discount =", discount)
print("Tax =", tax)
print("Total Cost =", total_cost)