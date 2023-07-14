class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def calculate_total_cost(self):
        total_cost = 0
        for product, quantity in self.items:
            total_cost += product.price * quantity
        return total_cost

    def clear_cart(self):
        self.items = []


class OnlineShop:
    def __init__(self):
        self.products = [
            Product("Phone", 999.99, 10),
            Product("Laptop", 1499.99, 5),
            Product("Headphones", 199.99, 20),
            Product("Keyboard", 149.99, 15),
            Product("Mouse", 79.99, 30)
        ]
        self.shopping_cart = ShoppingCart()

    def display_product_catalog(self):
        print("Available Products:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} - ${product.price:.2f} ({product.stock} in stock)")

    def add_product_to_cart(self, product_index, quantity):
        if product_index < 1 or product_index > len(self.products):
            print("Invalid product index.")
            return

        product = self.products[product_index - 1]

        if quantity <= 0:
            print("Invalid quantity.")
            return

        if product.stock < quantity:
            print("Insufficient stock.")
            return

        self.shopping_cart.add_item(product, quantity)
        product.stock -= quantity
        print("Product added to the cart.")

    def remove_product_from_cart(self, product_index):
        if product_index < 1 or product_index > len(self.shopping_cart.items):
            print("Invalid product index.")
            return

        product, quantity = self.shopping_cart.items[product_index - 1]
        self.shopping_cart.remove_item(product)
        product.stock += quantity
        print("Product removed from the cart.")

    def display_cart_contents(self):
        print("Shopping Cart Contents:")
        for i, (product, quantity) in enumerate(self.shopping_cart.items, 1):
            print(f"{i}. {product.name} - ${product.price:.2f} ({quantity} in cart)")

        total_cost = self.shopping_cart.calculate_total_cost()
        print(f"Total Cost: ${total_cost:.2f}")

    def process_order(self):
        if len(self.shopping_cart.items) == 0:
            print("Shopping cart is empty. Cannot process empty order.")
            return

        self.display_cart_contents()
        payment_method = input("Select payment method (cash, card, Venmo, Cash App): ")

        if payment_method == "cash":
            print("Payment successful! Order processed.")
        elif payment_method == "card":
            card_number = input("Enter 16-digit card number: ")
            pin = input("Enter card PIN: ")
            print("Payment successful! Order processed.")
        elif payment_method == "Venmo":
            venmo_username = input("Enter Venmo username: ")
            print("Payment successful! Order processed.")
        elif payment_method == "Cash App":
            cash_app_username = input("Enter Cash App username: ")
            print("Payment successful! Order processed.")
        else:
            print("Invalid payment method. Order cancelled.")
            return

        self.shopping_cart.clear_cart()

    def run(self):
        print("Welcome to the Online Shop!")

        while True:
            print("\nMenu:")
            print("1. View Products")
            print("2. Add Product to Cart")
            print("3. Remove Product from Cart")
            print("4. View Cart Contents")
            print("5. Process Order")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.display_product_catalog()
            elif choice == "2":
                try:
                    product_index = int(input("Enter the product index: "))
                    quantity = int(input("Enter the quantity: "))
                    self.add_product_to_cart(product_index, quantity)
                except ValueError:
                    print("Invalid input. Please enter a valid number for the product index and quantity.")
            elif choice == "3":
                try:
                    product_index = int(input("Enter the product index: "))
                    self.remove_product_from_cart(product_index)
                except ValueError:
                    print("Invalid input. Please enter a valid number for the product index.")
            elif choice == "4":
                self.display_cart_contents()
            elif choice == "5":
                self.process_order()
            elif choice == "6":
                print("Thank you for using the Online Shop!")
                break
            else:
                print("Invalid option. Please try again.")


shop = OnlineShop()
shop.run()
