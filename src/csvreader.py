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


# Example usage
# filename = "data.csv"
# reader = CSVReader(filename)
# data = reader.read_data()

# for row in data:
#     print(row)
