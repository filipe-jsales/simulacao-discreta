from src import csvreader
import simpy

file_product_ids = "products.csv"

class Product:
    def __init__(self):
        self.env = simpy.Environment()
        self.product_id = "product_id"
        self.name = "name"
        self.price = 1
        reader = csvreader.CSVReader(file_product_ids)
        self.data = reader.read_data()
        self.products_id = reader.transform_column_to_array(0)


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

    def get_product_ids(self):
        return self.products_id

# Usage example:
# env = simpy.Environment()
# product = Product(env, "p1", "Example Product", 10)
