import csv

cereals_filename = 'country_info.txt'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
        for value in row.values():
            print(value)
