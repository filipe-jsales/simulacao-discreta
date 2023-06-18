import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        data = []
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                data.append(row)
        return data

    def transform_last_column_to_array(self):
        data = self.read_data()
        last_column_array = []
        for row in data:
            last_column_value = float(row[-1])
            last_column_array.append(last_column_value)
        return last_column_array
    
    
# Example usage
# filename = "data.csv"
# reader = CSVReader(filename)
# data = reader.read_data()

# for row in data:
#     print(row)
