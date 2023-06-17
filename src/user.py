import simpy

class User:
    def __init__(self, env, user_id, birth_date, sex):
        self.env = env
        self.user_id = user_id
        self.birth_date = birth_date
        self.sex = sex
        self.user_actions = []

    def __str__(self):
        return f"User {self.user_id}: Birth Date - {self.birth_date}, Sex - {self.sex}"

    def add_action(self, order_id, action, time):
        self.user_actions.append((order_id, action, time))

    def perform_action(self, order_id, action, time):
        yield self.env.timeout(time)  # Simulate the time it takes to perform the action
        self.add_action(order_id, action, time)

# Usage example:
env = simpy.Environment()
user = User(env, "user123", "2000-01-01", "Male")

def user_behavior(user):
    yield env.timeout(10)  # Wait for 10 simulation time units
    yield from user.perform_action("order123", "Action 1", 5)  # Perform an action

env.process(user_behavior(user))
env.run(until=20)  # Run the simulation for 20 time units

# Print the user's actions
for action in user.user_actions:
    order_id, action_name, action_time = action
    print(f"Order ID: {order_id}, Action: {action_name}, Time: {action_time}")
