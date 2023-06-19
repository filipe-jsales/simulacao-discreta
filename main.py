from src import(courier, user, csvreader, dataprocessor, order, product)
import numpy as np
import simpy
from src.delivery import DeliverySimulation
#define wich file to read
file_courier_actions_new = "courier_actions_new.csv"
file_couriers = "couriers.csv"
file_orders = "orders.csv"
file_users = "users.csv"
file_user_actions = "user_actions.csv"

couriers = courier.Courier(1, '1990-01-01', 'M')

simulation = DeliverySimulation()

# Define the simulation duration
simulation_duration = 100  # Adjust the duration as needed

# Run the simulation
simulation.run_simulation(simulation_duration)











#tratamento de dados estatisticos
reader = csvreader.CSVReader(file_courier_actions_new)

data = reader.read_data()

csv_to_array = reader.transform_column_to_array(-1)
processor = dataprocessor.DataProcessor()

# processor.processAndRemoveOutliers(csv_to_array)
# processor.printInfoDados(csv_to_array)


# processor.plotFunction(csv_to_array)

# processor.getLen(csv_to_array)
