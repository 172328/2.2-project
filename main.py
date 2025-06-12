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

total_orders = [] #store all orders through the day
gst = 1.15
delivery_charge = 5

def display_menu():
    print("\nRangitoto Restaurant Menu")
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
        if len(order) >= 3:
            more = input("Would you like to order more? (y/n) ").lower()
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
        postcode = input("Enter your postcode (0620, 0630, and 0632 only): ")
        if postcode not in ["0620", "0630", "0632"]:
            print("Sorry, we do not deliver to that postcode, order canceled.")
        address = input("Enter your address: ")
    return{"name": name, "phone": phone, "delivery": delivery, "address": address}

def calculate_order(order_total, delivery):
    subtotal = sum(menu_items[item][1] * qty for item, qty in order_total.items())
    delivery_fee = delivery_charge if delivery == "d" else 0
    total = subtotal + delivery_charge
    gst_excluded = round(total / gst, 2)
    return total, gst_excluded, delivery_charge

def cancel_order():
    confirm = input("Cancel this order & restart? (y/n): ").lower()
    return confirm == "y"

while True:
    display_menu()
    order_total = select_menu()
    customer = customer_details()

    print("your order: ")
    for item_num, qty in order_total.items():
        name, price = menu_items[item_num]
        print(f"{name} x {qty} = ${price * qty}")
    if customer["delivery"] =="d":
        print("delivery: $5")

    if cancel_order():
        print("Order Cancelled, Restarting\n")
        continue

    total, gst_excl, delivery = calculate_order(order_total, customer["delivery"])

    print("\nTotal")
    print(f"Subtotal: ${total - delivery}")
    print(f"Delivery: ${delivery}")
    print(f"Total (GST included): ${total}")
    print(f"GST excluded: ${gst_excl}")

    total_orders.append({
        "customer": customer,
        "items": order_total,
        "total": total,
        "gst_excluded": gst_excl
    })

    again = input("Would you like to take another order? (y/n): ")
    if again != "y":
        break

print("Day Summary:")
for i, order in enumerate(total_orders, 1):
    print(f"\nOrder {i}")
    print(f"Customer: {order['customer']['name']}")
    print(f"Phone: {order['customer']['phone']}")
    print(f"Address {order['customer']['address']}")
    #calculate total orders
    print("Items Ordered:")
    for item_num, qty in order['items'].items():
        print(f"{menu_items[item_num][0]} x {qty}")
    print(f"\n Day Total: ${order['total']} (GST excluded: ${order['gst_excluded']})")

