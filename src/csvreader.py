import csv


class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        data = []
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row)
        return data

    def transform_column_to_array(self, column_index):
        data = self.read_data()
        column_array  = []
        for row in data:
            last_column_value = float(row[column_index])
            column_array .append(last_column_value)
        return column_array 
    