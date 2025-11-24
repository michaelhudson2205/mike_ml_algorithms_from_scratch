# Import libraries
from csv import reader
import os

print(os.getcwd())

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Load dataset
filename = '../data/pima-indians-diabetes.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, 
                                                                  len(dataset), 
                                                                  len(dataset[0])))

print(dataset[:5])  # Print first 5 rows of the dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string columns to float
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)

print(dataset[:5])  # Print first 5 rows after conversion

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Load iris dataset
filename = '../data/iris.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, 
                                                                  len(dataset), 
                                                                  len(dataset[0])))
print(dataset[0])  # Print first row of the dataset
# Convert string columns to float
for i in range(len(dataset[0]) - 1):
    str_column_to_float(dataset, i)
# Convert class column to integer
lookup = str_column_to_int(dataset, len(dataset[0]) - 1)
print('Class mapping: {0}'.format(lookup))
print(dataset[0])  # Print first row after conversion
