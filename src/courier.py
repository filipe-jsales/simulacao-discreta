
class Courier:
    def __init__(self, courier_id, birth_date, sex):
        self.courier_id = courier_id
        self.birth_date = birth_date
        self.sex = sex

    def __str__(self):
        return f"Courier {self.courier_id}: {self.sex}, born on {self.birth_date}"
