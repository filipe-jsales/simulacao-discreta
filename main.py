from src import(courier, user, csvreader, dataprocessor)
import statistics as st
from src.dataprocessor import DataProcessor

filename = "courier_actions_new.csv"
reader = csvreader.CSVReader(filename)
data = reader.read_data()

array_waiting_time_minutes_courier = reader.transform_last_column_to_array()
print(array_waiting_time_minutes_courier)





processor = DataProcessor()
processor.process_data(array_waiting_time_minutes_courier)
processor.printInfoDados(array_waiting_time_minutes_courier)