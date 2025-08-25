import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def list_products():
    """List all product in store"""
    product_line = best_buy.get_all_products()
    print("------")
    for i, product in enumerate(product_line, 1):
        print(f"{i}. ", end="")
        product.show()
    print("------\n")


def show_total_quantity():
    """Show total quantity of products in store"""
    total = best_buy.get_total_quantity()
    print(f"Total of {total} items in store\n")


def make_order():
    """Make order"""
    if not best_buy.get_all_products():
        print("No products available!")
        return

    shopping_list = []
    print("When you to finish order, enter empty text.")

    while True:
        available_products = best_buy.get_all_products()
        list_products()
        try:
            product_choice = input("Which product # do you want?: ")
            if product_choice == "":
                print("********")
                break

            product_index = int(product_choice) - 1
            if 0 <= product_index < len(available_products):
                product = available_products[product_index]
                quantity = int(input("What amount do you want?: "))

                # Validierung der Menge gegen verfügbaren Bestand
                if quantity <= product.quantity:
                    total_price_for_quantity = product.buy(quantity)
                    shopping_list.append((product, quantity, total_price_for_quantity))
                    print(f"Added {quantity} x {product.name} to cart")
                else:
                    print(f"Sorry, only {product.quantity} items available!")
            else:
                print("Invalid product number!")
        except ValueError:
            print("Please enter valid numbers!")

    if shopping_list:
        try:
            #total_price = best_buy.order(shopping_list)
            total_price = sum(item[2] for item in shopping_list)
            print(f"Order made! Total payment: ${total_price}\n")
        except ValueError as fehler:
            print(f"Order failed: {fehler}")


def start():
    """Main menu loop"""
    while True:
        print("   Store Menu\n"
              "   ----------\n"
              "1. List all products in store\n"
              "2. Show total amount of products in store\n"
              "3. Make an order\n"
              "4. Quit")
        choice = input("Please choose a number: ")
        if choice == "1":
            list_products()
        elif choice == "2":
            show_total_quantity()
        elif choice == "3":
            make_order()
        elif choice == "4":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")


if __name__ == '__main__':
    start()
