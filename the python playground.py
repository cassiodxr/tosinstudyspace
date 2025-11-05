item1 = input("Enter item name: ")
item1_price = float(input("Enter price of "+item1))
item1_num = float(input("Enter quantity of "+item1))
item1_total = item1_price * item1_num

item2 = input("Enter item name: ")
item2_price = float(input("Enter price of "+item2))
item2_num = float(input("Enter quantity of "+item2))
item2_total = item2_price * item2_num

item3 = input("Enter item name: ")
item3_price = float(input("Enter price of "+item3))
item3_num = float(input("Enter quantity of "+item3))
item3_total = item3_price * item3_num

discount_status = None

discount = input("Are you a Senior Citizen? (yes/no) ")
if discount.lower() == "y" or "yes":
    discount_status = True

subtotal = (item1_total + item2_total + item3_total)
original_total = subtotal

# cap discount at 125
if discount_status == True:
    discount_check = original_total * 0.05
    if discount_check > 125:
        subtotal -= 125
        discount_check = 125
    else:
        subtotal -= discount_check

VAT = subtotal * 0.12
subtotal += VAT

print("Total Amount:",subtotal)

balance = float(input("Enter amount of cash: "))
if balance < subtotal:
    print("Insufficient balance.")
else:
    print("Change:",round(balance-subtotal,2))