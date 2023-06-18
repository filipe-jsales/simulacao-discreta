from src import(courier, user, csvreader)
import statistics as st
from src.dataprocessor import DataProcessor
# import matplotlib.pyplot as plt
# import math as m

filename = "courier_actions_new.csv"
reader = csvreader.CSVReader(filename)
data = reader.read_data()

array_waiting_time_minutes_courier = reader.transform_last_column_to_array()
print(array_waiting_time_minutes_courier)


DataProcessor.process_data(array_waiting_time_minutes_courier)
