class Product:
    """Product class"""
    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product."""
        if name is None or name == "":
            raise ValueError("Name cannot be None or empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Display the product."""
        status = "Active" if self.active else "Inactive"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}")

    def buy(self, quantity: int) -> float:
        """Buy a product."""
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
