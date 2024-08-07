#PRESENTACION DE CASO SANOFI.
#AGUILAR BUSTILLOS ALAN RODRIGO.

#Creación de un diccionario de articulos con la asginacion de sus precios respectivamente:
item_prices = {
    "apple": 1.25,
    "banana": 0.75,
    "orange": 1.50,
    "grapes": 2.00,
    "chocolate": 3.50
}

#creación del carrito de compras empleando una lista que se encuentra vacia para poder ingresar los articulos al carrito de compras:
shopping_cart = []

# creación de un bucle para ingresar los items al shoppint cart, el cual se encuentra condicionado a que se 
# ingrese un articulo que ya se encuentre dentro deñ diccionario creado, o de lo contrario se le pide al usuario el ingresar un item valido
# al ingresar la palabra 'done' el bucle termina, causando el cierre del carrito de compras:
while True:
    item = input("Enter an item (or 'done' to finish): ").lower()
    if item == "done":
        break
    elif item in item_prices:
        shopping_cart.append(item)
    else:
        print("Item not found. Please choose a valid item.")

# se realiza el calculo del costo total, realizando la suma de los articulos que se seleccionaron con aterioridad:
total_cost = sum(item_prices[item] for item in shopping_cart)


print("\nShopping Cart:")
for item in shopping_cart:
    print(f" - {item} (${item_prices[item]})")

#impresion del total del carrito:
print(f"\nTotal Cost: ${total_cost}")