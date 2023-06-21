from src import(csvreader,dataprocessor )
import argparse
import simpy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import statistics as st


class DeliverySystem:
    def __init__(self, env: simpy.Environment, n_weeks: int, n_couriers: int, n_deliveries: int):
        self.env = env
        self.couriers = simpy.Resource(env, n_couriers)
        self.n_weeks = n_weeks
        self.n_deliveries = n_deliveries
        self.successful_deliveries = {}
        self.refused_deliveries = {}
        self.weekly_stats = {}

    def get_deliver_time_date(self):
        file_courier_actions_new = "courier_actions_new.csv"
        reader = csvreader.CSVReader(file_courier_actions_new)
        csv_to_array = reader.transform_column_to_array_str(3)
        return csv_to_array 
    
    def get_waiting_time_minutes(self):
        file_courier_actions_new = "courier_actions_new.csv"
        reader = csvreader.CSVReader(file_courier_actions_new)
        csv_to_array = reader.transform_column_to_array(-1)
        return csv_to_array 

    def get_product_name(self):
        file_products = "products.csv"
        reader = csvreader.CSVReader(file_products)
        csv_to_array = reader.transform_column_to_array_str(1)
        return csv_to_array 

    def delivery_process(self, courier_id):
        self.successful_deliveries[courier_id] = 0
        self.refused_deliveries[courier_id] = 0
        array_time = self.get_waiting_time_minutes()
        product_names = self.get_product_name()
        quantile = st.quantiles(array_time)
        third_quantile = quantile[-1]

        for index, delivery in enumerate(range(self.n_deliveries)):
            success_probability = self.couriers.capacity / (self.couriers.capacity + 1)
            random_product_index = random.randint(0, len(product_names) - 1)
            product_name = product_names[random_product_index]
            print('ARRAY TIME', array_time[index])
            if array_time[index] < third_quantile or random.random() < success_probability:
                self.successful_deliveries[courier_id] += 1
                current_time = array_time[index]
                print(f"Courier_id: {courier_id} successfully delivered {product_name} at {current_time}")
            else:
                self.refused_deliveries[courier_id] += 1
                current_time = array_time[index]
                print(f"The user canceled the order {product_name} at time {current_time}")

            yield self.env.timeout(1)

    
    def get_courier_id(self):
        file_courier_actions_new = "courier_actions_new.csv"
        reader = csvreader.CSVReader(file_courier_actions_new)
        csv_to_array = reader.transform_column_to_array(0)
        return csv_to_array 

    def run_delivery_system(self):
        courier_ids = self.get_courier_id()
        num_couriers = min(len(courier_ids), self.couriers.capacity)

        for week in range(1, self.n_weeks + 1):
            print(f"Week {week}:")
            weekly_successful_deliveries = 0
            weekly_refused_deliveries = 0

            for i in range(1, num_couriers + 1):
                courier_id = courier_ids[i - 1]  
                self.env.process(self.delivery_process(courier_id))
                yield self.env.timeout(1)

                weekly_successful_deliveries += self.successful_deliveries[courier_id]
                weekly_refused_deliveries += self.refused_deliveries[courier_id]

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


def simulate_delivery_system(n_weeks, n_couriers, n_deliveries):
    env = simpy.Environment()
    delivery_system = DeliverySystem(env, n_weeks, n_couriers, n_deliveries)
    env.process(delivery_system.run_delivery_system())
    env.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulator for a delivery system.")
    parser.add_argument("-w", "--weeks", type=int, default=4, help="Number of weeks to simulate.")
    parser.add_argument("-d", "--couriers", type=int, default=100, help="Number of delivery couriers.")
    parser.add_argument("-p", "--deliveries", type=int, default=2, help="Number of deliveries per driver.")
    args = parser.parse_args()
    
    simulate_delivery_system(args.weeks, args.couriers, args.deliveries)
    file_courier_actions_new = "courier_actions_new.csv"
    file_couriers = "couriers.csv"
    file_orders = "orders.csv"
    file_users = "users.csv"
    file_user_actions = "user_actions.csv"


    reader = csvreader.CSVReader(file_courier_actions_new)

    data = reader.read_data()

    csv_to_array = reader.transform_column_to_array(-1)
    processor = dataprocessor.DataProcessor()
    processor.processAndRemoveOutliers(csv_to_array)
    processor.printInfoDados(csv_to_array)


    processor.plotFunction(csv_to_array)

    processor.getLen(csv_to_array)