class Store:
    """Store class"""
    def __init__(self, product_list=None):
        """initialize the store"""
        if product_list is None:
            self.products = []
        else:
            self.products = product_list

    def add_product(self, product):
        """add a product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """remove a product from the store"""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """return the total quantity of the store"""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """return all the products in the store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """order the store"""
        total_price = 0
        for product, quantity in shopping_list:
            try:
                # Hier rufen wir die buy-Methode des Produkts auf
                total_price += product.buy(quantity)
            except ValueError as fehler:
                print(f"Error ordering {product.name}: {fehler}")
                raise fehler
        return total_price
