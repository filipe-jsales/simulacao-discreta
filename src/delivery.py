import simpy
from src.courier import Courier
from src.order import Order
from src.product import Product
class DeliverySimulation:
    def __init__(self):
        self.env = simpy.Environment()
        self.courier_list = []
        self.num_couriers = 10  
        self.products_id = Product().get_product_ids()
        
        for i in range(self.num_couriers):
            courier = Courier(i, "birth_date", "sex")
            self.courier_list.append(courier)

    def generate_orders(self):
        order_id = 1
        while True:
            order = self.generate_order(order_id)
            order_id += 1

            # available_courier = self.find_available_courier()
            # if available_courier is not None:
            #     self.allocate_order_to_courier(order, available_courier)

            yield self.env.timeout(10)  

    def generate_order(self, order_id):
        # Generate a new order with its corresponding attributes
        creation_time = self.env.now
        product_ids = self.products_id  # Implement this method to generate product IDs for the order

        # Create an Order object
        order = Order(order_id, creation_time, product_ids)
        return order


    def find_available_courier(self):
        for courier in self.courier_list:
            if courier.is_available():
                return courier
        return None

    def allocate_order_to_courier(self, order, courier):
        courier.accept_order(order)

    def run_simulation(self, simulation_duration):
        self.env.process(self.generate_orders())

        self.env.run(until=simulation_duration)