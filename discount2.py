
# DISCOUNT PRICE CALCULATOR FOR SHOPING MALL ------------- CLASS 7 FINAL PROJECT

from datetime import datetime


discount_rate = 0.10
sales_tax_rate = 0.06

subtotal = float(input("please enter subtotal:"))

current_date_and_time = datetime.now()

weekday = current_date_and_time.weekday()

# [0-mon , 1-tue , 2-wed , 3-thu , 4-fri ,5-sat ,6-sun]

print(weekday)
# 
if (weekday == 6 or weekday == 2):
    discount = round(subtotal * discount_rate, 2)
    print(f"Discount amount:{discount:.2f}")
    subtotal  = subtotal - discount 

sales_tax = round(subtotal* sales_tax_rate,2)
print(f"Sales tax amount: {sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: {total:.2f}")