class Courier:
    def __init__(self, courier_id, birth_date, sex, courier_actions=None):
        self.courier_id = courier_id
        self.birth_date = birth_date
        self.sex = sex
        self.courier_actions = courier_actions if courier_actions else []

    def __str__(self):
        return f"Courier {self.courier_id}: {self.sex}, born on {self.birth_date}"

    def add_action(self, order_id, action, accept_time, deliver_time, waiting_time, waiting_time_minutes):
        self.courier_actions.append((order_id, action, accept_time, deliver_time, waiting_time, waiting_time_minutes))
