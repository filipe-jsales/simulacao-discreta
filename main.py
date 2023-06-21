from src import(csvreader,dataprocessor )
import argparse
import simpy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random


file_courier_actions_new = "courier_actions_new.csv"
file_couriers = "couriers.csv"
file_orders = "orders.csv"
file_users = "users.csv"
file_user_actions = "user_actions.csv"


#tratamento de dados estatisticos
reader = csvreader.CSVReader(file_courier_actions_new)

data = reader.read_data()

csv_to_array = reader.transform_column_to_array(-1)
processor = dataprocessor.DataProcessor()

class DeliverySystem:
    def __init__(self, env: simpy.Environment, n_weeks: int, n_drivers: int, n_deliveries: int):
        self.env = env
        self.drivers = simpy.Resource(env, n_drivers)
        self.n_weeks = n_weeks
        self.n_deliveries = n_deliveries
        self.successful_deliveries = {}
        self.refused_deliveries = {}
        self.weekly_stats = {}

    def delivery_process(self, driver_id):
        self.successful_deliveries[driver_id] = 0
        self.refused_deliveries[driver_id] = 0

        for delivery in range(self.n_deliveries):
            success_probability = self.drivers.capacity / (self.drivers.capacity + 1)
            if random.random() < success_probability:
                self.successful_deliveries[driver_id] += 1
                current_time = self.env.now + 4
                print(f"Driver {driver_id} successfully delivered package {delivery} at time {current_time}")
            else:
                self.refused_deliveries[driver_id] += 1

            yield self.env.timeout(1)

    def run_delivery_system(self):
        for week in range(1, self.n_weeks + 1):
            print(f"Week {week}:")
            weekly_successful_deliveries = 0
            weekly_refused_deliveries = 0

            for driver_id in range(1, self.drivers.capacity + 1):
                self.env.process(self.delivery_process(driver_id))
                yield self.env.timeout(1)

                weekly_successful_deliveries += self.successful_deliveries[driver_id]
                weekly_refused_deliveries += self.refused_deliveries[driver_id]

            self.weekly_stats[week] = {
                "Successful Deliveries": weekly_successful_deliveries,
                "Refused Deliveries": weekly_refused_deliveries
            }

        self.get_delivery_stats()

    def get_delivery_stats(self):
        print("\nDelivery Statistics:")
        weeks = []
        success_percentages = []
        refused_percentages = []

        for week in self.weekly_stats:
            weeks.append(week)
            weekly_successful_deliveries = self.weekly_stats[week]["Successful Deliveries"]
            weekly_refused_deliveries = self.weekly_stats[week]["Refused Deliveries"]
            total_deliveries = weekly_successful_deliveries + weekly_refused_deliveries
            success_percentage = (weekly_successful_deliveries / total_deliveries) * 100
            refused_percentage = (weekly_refused_deliveries / total_deliveries) * 100

            success_percentages.append(success_percentage)
            refused_percentages.append(refused_percentage)

            print(f"Week {week}:")
            print(f"Successful Deliveries: {weekly_successful_deliveries} ({success_percentage}%)")
            print(f"Refused Deliveries: {weekly_refused_deliveries} ({refused_percentage}%)\n")

        self.plot_delivery_stats(weeks, success_percentages, refused_percentages)

    def plot_delivery_stats(self, weeks, success_percentages, refused_percentages):
        plt.figure(figsize=(10, 5))

        delivery_success_data = pd.DataFrame({'Week':weeks, 'Successful Delivery':success_percentages, 'Refused Delivery':refused_percentages})
        df_melted = pd.melt(delivery_success_data, id_vars=['Week'], value_vars=['Successful Delivery', 'Refused Delivery'],
                            var_name='tipo', value_name='quantidade')
        sns.set(style="whitegrid")
        sns.barplot(x='Week', y='quantidade', hue='tipo', data=df_melted)
        plt.xlabel('Weeks')
        plt.ylabel('Percentage')
        plt.title('Delivery Statistics')
        plt.legend()
        plt.show()


def simulate_delivery_system(n_weeks, n_drivers, n_deliveries):
    env = simpy.Environment()
    delivery_system = DeliverySystem(env, n_weeks, n_drivers, n_deliveries)
    env.process(delivery_system.run_delivery_system())
    env.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulator for a delivery system.")
    parser.add_argument("-w", "--weeks", type=int, default=4, help="Number of weeks to simulate.")
    parser.add_argument("-d", "--drivers", type=int, default=10, help="Number of delivery drivers.")
    parser.add_argument("-p", "--deliveries", type=int, default=48, help="Number of deliveries per driver.")
    args = parser.parse_args()

    print(csv_to_array)
    simulate_delivery_system(args.weeks, args.drivers, args.deliveries)
