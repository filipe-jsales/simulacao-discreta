import simpy

class User:
    def __init__(self, user_id, birth_date, sex):
        self.user_id = user_id
        self.birth_date = birth_date
        self.sex = sex
        self.user_actions = []
        self.t_espera_total = 0
