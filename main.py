from multiprocessing.connection import address_type

menu_items={
    1: ("Kawakawa Spritzer", 6),
    2: ("Pork and Puha Slider", 6),
    3: ("Horopito Fish Collars", 6),
    4: ("Kawakawa Mussels", 6),
    5: ("Taro and Coconut Fritters", 6),
    6: ("Kumara and Fennel Salad", 6),
    7: ("Paua and Prawn Dumplings", 9),
    8: ("Kina Canapes", 9),
    9:("Kumara and Truffle Ravioli", 9),
    10:("Manuka Smoked Salmon", 9),
    11: ("Paua Porridge", 9)
}

total_orders = []

def display_menu():
    print("Rangitoto Restaurant Menu")
    for number, (name, price) in menu_items.items():
        print(f"{number}. {name} - ${price}")

def select_menu():
    order = {}
    while True:
        try:
            choice = int(input("Enter item number you would like to order "))
            if choice in menu_items:
                quantity = int(input("How many would you like? "))
                if choice in order:
                    order[choice] += quantity
                else:
                    order[choice] = quantity
            else:
                print("That's not on the menu! Try again.")
        except ValueError:
            print("Please enter a number.")
        if len(order) >= 1:
            more = input("Would you like to order more? (y/n)").lower()
            if more != "y":
                break

    return order

def customer_details():
    print("Customer Info")
    name = input("Name: ")
    phone = input("Phone Number: ")
    delivery = input("Would you like delivery or pickup? (d/p): ").lower()
    address = ""
    if delivery == "d":
        address = input("Enter your address: ")
    return{"name": name, "phone": phone, "delivery": delivery, "address": address}

display_menu()
order = select_menu()
customer_details()

print("your order: ", order)
print("Details: ")