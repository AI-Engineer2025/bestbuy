import products

class Store:
    def __init__(self, product_list=None):
        if product_list is None:
            self.products = []
        else:
            self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            try:
                # Hier rufen wir die buy-Methode des Produkts auf
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error ordering {product.name}: {e}")
        return total_price


"""# Test
if __name__ == '__main__':
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products_list = best_buy.get_all_products()
    print(best_buy.get_total_quantity())

    # Testbestellung
    if len(products_list) >= 2:
        print(best_buy.order([(products_list[0], 1), (products_list[1], 2)]))"""