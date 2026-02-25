# class ShoppingCart:
#     def __init__(self):
#         self.cart = {}

#     def add_item(self, product, price, quantity=1):
#         if product in self.cart:
#             self.cart[product]['quantity'] += quantity
#         else:
#             self.cart[product] = {'price': price, 'quantity': quantity}
#         print(f"{quantity} x {product} added to cart.")

#     def remove_item(self, product, quantity=1):
#         if product in self.cart:
#             if self.cart[product]['quantity'] > quantity:
#                 self.cart[product]['quantity'] -= quantity
#             else:
#                 del self.cart[product]
#             print(f"{product} removed from cart.")
#         else:
#             print("Item not found in cart.")

#     def view_cart(self):
#         if not self.cart:
#             print("Your cart is empty.")
#             return
        
#         print("\n🛒 Your Cart:")
#         total = 0
#         for product, details in self.cart.items():
#             item_total = details['price'] * details['quantity']
#             total += item_total
#             print(f"{product} - ${details['price']} x {details['quantity']} = ${item_total}")
        
#         print(f"\nTotal: ${total}")

#     def checkout(self):
#         if not self.cart:
#             print("Cart is empty. Add items before checkout.")
#             return
        
#         self.view_cart()
#         print("\n✅ Checkout successful! Thank you for shopping.")
#         self.cart.clear()


# # Sample Product Catalog
# products = {
#     "Laptop": 800,
#     "Phone": 500,
#     "Headphones": 100,
#     "Keyboard": 50
# }


# def main():
#     cart = ShoppingCart()

#     while True:
#         print("\n==== Online Store ====")
#         print("1. View Products")
#         print("2. Add to Cart")
#         print("3. Remove from Cart")
#         print("4. View Cart")
#         print("5. Checkout")
#         print("6. Exit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             print("\nAvailable Products:")
#             for product, price in products.items():
#                 print(f"{product} - ${price}")

#         elif choice == "2":
#             product = input("Enter product name: ")
#             if product in products:
#                 quantity = int(input("Enter quantity: "))
#                 cart.add_item(product, products[product], quantity)
#             else:
#                 print("Product not found.")

#         elif choice == "3":
#             product = input("Enter product name to remove: ")
#             quantity = int(input("Enter quantity to remove: "))
#             cart.remove_item(product, quantity)

#         elif choice == "4":
#             cart.view_cart()

#         elif choice == "5":
#             cart.checkout()

#         elif choice == "6":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option. Try again.")


# if __name__ == "__main__":
#     main()


# Product list
products = {
    "Laptop": 800,
    "Phone": 500,
    "Headphones": 100,
    "Keyboard": 50
}

cart = {}

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for item in products:
            print(item, "-", products[item])

    elif choice == "2":
        item = input("Enter product name: ")
        if item in products:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("Item added!")
        else:
            print("Product not found.")

    elif choice == "3":
        total = 0
        for item in cart:
            price = products[item]
            qty = cart[item]
            print(item, "-", qty, "x", price)
            total += price * qty
        print("Total =", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
