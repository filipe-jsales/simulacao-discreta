class Order:
    def __init__(self, order_id, creation_time, product_ids):
        self.order_id = order_id
        self.creation_time = creation_time
        self.product_ids = product_ids

    def __str__(self):
        return f"Order {self.order_id}: Creation Time - {self.creation_time}, Product IDs - {self.product_ids}"
