menu = {
    'Pasta':80,
    "Coffee":50,
    "Salad":40,
    "Sandwich":30,
    "Burger":20,
    "Pizza":10,
    "Soda":10,
}

print("Welcome to the python Restaurent menu")


print(
    "Our menu is:\n"
    "Pasta   :Rs80\n"
    "Coffee  :Rs50\n"
    "Salad   :Rs40\n"
    "Sandwich:Rs30\n"
    "Burger  :Rs20\n"
    "Pizza   :Rs10\n"
    "Soda    :Rs10\n"
)
order_total=0

item1 =input("Enter the menu to order:")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your {item1} is added to your order")
else:
    print(f"Ordered {item1} is not in the menu")


another_order = input("Do you want to order second time? (yes/no)")
if another_order == "yes":
    item2 = input("Enter the name of the second item: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your {item2} is added to your order")
    else:
        print(f"Ordered {item2} is not in the menu")

print(f"Your total order amount is {order_total}")

