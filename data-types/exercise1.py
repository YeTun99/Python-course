product_name=input("Please enter product name:")
product_price=int(input("Please enter product price:"))
product_qty=int(input("Please enter product quantity:"))
product_discount=int(input("Please enter product discount:"))

subtotal=product_price*product_qty
discount=(subtotal*product_discount)/100
total=(subtotal)-discount
underline="_________________"

print(f"Product name:{product_name}")
print(f"Product price:{product_price}")
print(f"Product quantity:{product_qty}")
print(underline)
print(f"Total:{total}")

