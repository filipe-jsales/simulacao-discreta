class User:
    def __init__(self, user_id, birth_date, sex, user_actions=None):
        self.user_id = user_id
        self.birth_date = birth_date
        self.sex = sex
        self.user_actions = user_actions if user_actions else []

    def __str__(self):
        return f"User {self.user_id}: Birth Date - {self.birth_date}, Sex - {self.sex}"

    def add_action(self, order_id, action, time):
        self.user_actions.append((order_id, action, time))