# Mini Shopping Bill

product_name = (input("Enter your product name : "))
product_price = (int(float(input("Enter Your product price : "))))
quantity = (int(input("Enter your quantity : ")))

total = product_price * quantity

print(product_name)
print(quantity)
print("total bill", total)