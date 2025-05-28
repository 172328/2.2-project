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

def display_menu():
    print("Rangitoto Restaurant Menu")
    for number, (name, price) in menu_items.items():
        print(f"{number}. {name} - ${price}")

def select_menu():


display_menu()