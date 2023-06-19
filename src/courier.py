from src import csvreader
import simpy

file_courier_actions_new = "courier_actions_new.csv"


class Courier:
    def __init__(self, courier_id, birth_date, sex):
        self.courier_id = courier_id
        self.birth_date = birth_date
        self.sex = sex
        self.env = simpy.Environment()
        self.action_process = self.env.process(self.courier_actions())
        self.action = ""
        reader = csvreader.CSVReader(file_courier_actions_new)
        self.data = reader.read_data()
        self.couriers_id = reader.transform_column_to_array(0)
        self.waiting_time_minutes = reader.transform_column_to_array(-1)
        self.is_available = True

    def __str__(self):
        return f"Courier {self.courier_id}: {self.sex}, born on {self.birth_date}"

    def courier_actions(self):
        while True:
            order_id, action, accept_time, deliver_time, waiting_time = yield self.env.process(self.add_action())
            # Perform necessary actions with the order_id, action, etc.
            # Example: Update courier's state, log data, etc.

    def add_action(self):
        yield self.env.timeout(0)  # Initial delay before starting actions

        # Simulate actions over time using yield statements
        # Example: Simulate accepting an order
        courier_index = self.couriers_id.index(self.courier_id)  # Index of the courier in the array
        order_id = self.data[courier_index]["order_id"]  # Fetch the order_id from the data array
        action = "accept_order"
        accept_time = self.env.now
        yield self.env.timeout(5)  # Simulate processing time
        deliver_time = self.env.now

        # Example: Simulate waiting time
        waiting_time = self.waiting_time_minutes

        print("Courier", self.courier_id, "has accepted order", order_id, "at", accept_time, "and delivered it at", deliver_time, "after waiting for", waiting_time, "minutes")
        # Return the generated data to the courier_actions method
        return order_id, action, accept_time, deliver_time, waiting_time

    def getCouriersArray(self):
        return self.couriers_id
    

    def getCourierId(self):
        print(self.courier_id)
        return self.courier_id

    def accept_order(self, order="accept_order"):
        self.action = order

    def find_available_courier(self):
        for courier in self.courier_list:
            if courier.is_available():
                return courier
        return None