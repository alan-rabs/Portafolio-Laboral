item_prices = {
    "apple": 1.25,
    "banana": 0.75,
    "orange": 1.50,
    "grapes": 2.00,
    "chocolate": 3.50
}

shopping_cart = {}
while True:
    item = input("Enter an item (or 'done' to finish): ").lower()
    if item == "done":
        break
    elif item in item_prices:
        # modificacion para indicar cuantas unidades de un mismo producto se añadiran al carrito de compras:
        quantity = int(input(f"How many {item}s would you like to add? "))
        if item in shopping_cart:
            shopping_cart[item] += quantity
        else:
            shopping_cart[item] = quantity
    else:
        print("Item not found. Please choose a valid item.")

total_cost = sum(item_prices[item] * quantity for item, quantity in shopping_cart.items())

print("\nShopping Cart:")
for item, quantity in shopping_cart.items():
    print(f" - {item} x{quantity} (${item_prices[item] * quantity:.2f})")
print(f"\nTotal cost: ${total_cost:.2f}")