import simpy

class Order:
    def __init__(self, order_id, creation_time, product_ids):
        self.order_id = order_id
        self.creation_time = creation_time
        self.product_ids = product_ids
        self.env = simpy.Environment()
        self.action_process = self.env.process(self.order_actions())

    def __str__(self):
        return f"Order {self.order_id}: Creation Time - {self.creation_time}, Product IDs - {self.product_ids}"

    def order_actions(self):
        while True:
            action, action_time = yield self.env.process(self.add_action())
            # Perform necessary actions based on the action and action_time
            # Example: Update order's state, log data, etc.

    def add_action(self):
        yield self.env.timeout(0)  # Initial delay before starting actions

        # Simulate actions over time using yield statements
        # Example: Simulate processing the order
        action = "process"
        action_time = self.env.now
        yield self.env.timeout(10)  # Simulate processing time

        # Example: Simulate another action
        action = "another_action"
        action_time = self.env.now
        yield self.env.timeout(5)  # Simulate another action time

        # Return the generated data to the order_actions method
        return action, action_time
