import simpy
class Product:
    def __init__(self, env, product_id, name, price):
        self.env = env
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Price: {self.price}"

    def purchase(self, user, quantity):
        total_price = self.price * quantity
        if user.balance >= total_price:
            user.balance -= total_price
            yield self.env.timeout(1)  # Simulate the time it takes to process the purchase
            user.add_action(self.product_id, f"Purchased {quantity} {self.name}(s)", 1)
        else:
            user.add_action(self.product_id, "Insufficient balance", 0)

# Usage example:
env = simpy.Environment()
product = Product(env, "p1", "Example Product", 10)
