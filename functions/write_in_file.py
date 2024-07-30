import json


def write_in_file(result):
    with open('Parsing/vacancies/vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


    print(f'{len(result)} вакансий записано в файл vacancies.json')