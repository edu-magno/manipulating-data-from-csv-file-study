import csv
from typing import List

csv_filename = 'characters.csv'


def create_header_of_csv(fieldnames: List, filename: str):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def get_character_id(filename) -> int:
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        list_reader = list(reader)
        print(list_reader)
        if list_reader == []:
            return 1
        id_of_last_line = list_reader[-1].get('id', 0)
        return int(id_of_last_line) + 1


def create_character(filename: str, name: str, intelligence: str, power: str, strength: str, agility: str):
    fieldnames = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        reader_list = list(reader)
        if reader_list == []:
            print('created header in csv')
            create_header_of_csv(fieldnames, filename)

    id_character = get_character_id(filename)

    with open(filename, 'a', newline='') as file:

        writer = csv.DictWriter(
            file, fieldnames=fieldnames)

        writer.writerow({'id':  id_character, 'name': name, 'intelligence': intelligence,
                         'power': power, 'strength': strength, 'agility': agility})

    with open(filename, 'r', newline='') as file:
        read = csv.DictReader(file)
        return list(read)[-1]


def find_character_by_id(filename, character_id):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row_id = row.get('id')
            if int(row_id) == character_id:
                return row

        return None


def find_all_character(filename, **kwargs):
    list_of_characters_match = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        items = kwargs.items()
        for row in reader:
            for item in items:
                row_key = row.get(item[0])
                if row_key == item[1]:
                    list_of_characters_match.append(row)

    return list_of_characters_match


def delete_character(filename, character_id):
    fieldnames = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']
    rows = []
    with open(filename, 'r+', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row_id = row.get('id')
            if int(row_id) != character_id:
                rows.append(row)

    with open(filename, 'w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_character(filename, character_id, **kwargs):
    fieldnames = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']
    rows = []
    with open(filename, 'r+', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    for item in rows:
        item_id = item.get('id')
        if int(item_id) == character_id:
            item.update(kwargs)

    with open(filename, 'w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
