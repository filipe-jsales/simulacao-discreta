from src import(courier, user, csvreader, dataprocessor)

filename = "courier_actions_new.csv"
reader = csvreader.CSVReader(filename)
data = reader.read_data()

array_waiting_time_minutes_courier = reader.transform_last_column_to_array()

processor = dataprocessor.DataProcessor()
processor.processAndRemoveOutliers(array_waiting_time_minutes_courier)
processor.printInfoDados(array_waiting_time_minutes_courier)


processor.plotFunction(array_waiting_time_minutes_courier)

