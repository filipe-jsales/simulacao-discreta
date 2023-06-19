from src import(courier, user, csvreader, dataprocessor)

#define wich file to read
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
