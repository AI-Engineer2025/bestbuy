class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if name is None or name == "":
            raise ValueError("Name cannot be None or empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        status = "Active" if self.active else "Inactive"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


# Testcode
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()