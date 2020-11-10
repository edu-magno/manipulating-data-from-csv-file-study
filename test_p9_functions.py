from main import *
import csv

file_path = 'characters.csv'


def test_create_character():
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        list_reader = list(reader)
        last_id = int(list_reader[-1].get('id')) + 1
        result = create_character(
            'characters.csv', 'coisa', '7', '10', '10', '5')
        expected = {'id': str(last_id), 'name': 'coisa', 'intelligence': '7',
                    'power': '10', 'strength': '10', 'agility': '5'}

        assert expected == result


def test_find_character_by_id():
    result = find_character_by_id(file_path, 4)
    expected = {'id': '4', 'name': 'coisa', 'intelligence': '7',
                'power': '10', 'strength': '10', 'agility': '7'}

    assert expected == result


def test_all_characters():
    with open(file_path, 'r', newline='') as file:

        result = find_all_characters(
            file_path, **{'agility': '2', 'strength': '1'})
        expected = [
            {'id': '16', 'name': 'coisa', 'intelligence': '7',
             'power': '10', 'strength': '1', 'agility': '2'},
            {'id': '17', 'name': 'coisa', 'intelligence': '7',
             'power': '10', 'strength': '1', 'agility': '2'}
        ]

        assert expected == result


def test_delete_character():
    result = delete_character(file_path, 2)
    expected = False

    assert expected == result


def test_update_character():
    result = update_character(file_path, 5, **{'agility': '3', 'power': '6'})
    expected =  {'id': '5', 'name': 'coisa', 'intelligence': '7',
             'power': '6', 'strength': '3', 'agility': '3'}

    assert expected == result