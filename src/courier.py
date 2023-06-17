import simpy

class Courier:
    def __init__(self, courier_id, birth_date, sex):
        self.courier_id = courier_id
        self.birth_date = birth_date
        self.sex = sex
        self.env = simpy.Environment()
        self.action_process = self.env.process(self.courier_actions())

    def __str__(self):
        return f"Courier {self.courier_id}: {self.sex}, born on {self.birth_date}"

    def courier_actions(self):
        while True:
            order_id, action, accept_time, deliver_time, waiting_time, waiting_time_minutes = yield self.env.process(self.add_action())
            # Perform necessary actions with the order_id, action, etc.
            # Example: Update courier's state, log data, etc.

    def add_action(self):
        yield self.env.timeout(0)  # Initial delay before starting actions

        # Simulate actions over time using yield statements
        # Example: Simulate accepting an order
        order_id = 1
        action = "accept"
        accept_time = self.env.now
        yield self.env.timeout(5)  # Simulate processing time
        deliver_time = self.env.now

        # Example: Simulate waiting time
        waiting_time = self.env.now - accept_time
        waiting_time_minutes = waiting_time / 60

        # Return the generated data to the courier_actions method
        return order_id, action, accept_time, deliver_time, waiting_time, waiting_time_minutes
