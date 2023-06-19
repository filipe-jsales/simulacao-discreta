import simpy
from src import product

class Order:
    def __init__(self, order_id, creation_time, product_ids):
        self.order_id = order_id
        self.creation_time = creation_time
        self.product_ids = product_ids
        self.env = simpy.Environment()
        self.action_process = self.env.process(self.order_actions())
        self.products = product.Product().get_product_ids()

    def __str__(self):
        return f"Order {self.order_id}: Creation Time - {self.creation_time}, Product IDs - {self.product_ids}"

    def order_actions(self):
        while True:
            action, action_time = yield self.env.process(self.add_action())

    def add_action(self):
        yield self.env.timeout(0)  

        action = "process"
        action_time = self.env.now
        yield self.env.timeout(10)

        action = "another_action"
        action_time = self.env.now
        yield self.env.timeout(5)  

        return action, action_time
    
    def get_product_ids(self):
        product_ids = self.products
        return product_ids

