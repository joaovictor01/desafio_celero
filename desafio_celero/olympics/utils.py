"""Olympics utils."""
import csv


def csv_to_json(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        data_list = list()
        for row in reader:
            data_list.append(row)
        data = [dict(zip(data_list[0], row)) for row in data_list]
        data.pop(0)
    return data
