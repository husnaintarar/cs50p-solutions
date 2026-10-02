Items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

for user_input in Items:
    try:
        user_input = input("Item: ").title()

        if user_input == "": 
            break
        if user_input in Items:
            current_price = Items[user_input]
            price += current_price
            print(f"Total: ${price:.2f}")
        else:
            continue
    except EOFError:
        break
