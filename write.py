import csv
import json


def write_csv(empl_data):
    with open('database.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for empl in empl_data:
            writer.writerow(empl.values())

# def write_json(empl_data):
#      with open('database02.json', 'w', encoding='utf-8') as file:
#         for empl in empl_data:
#             file.write(json.dumps(empl) + '\n')

def write_json(empl_data):
    with open('database02.json', 'w') as outfile:
        json.dump(empl_data, outfile)

