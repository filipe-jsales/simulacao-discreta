from src import(courier, user, csvreader)

filename = "couriers.csv"
reader = csvreader.CSVReader(filename)

data = reader.read_data()

for row in data:
    print(row)
