from functions.get_vacancies import get_vacancies
from functions.parse_vacancies import parse_vacancies
from functions.write_in_file import write_in_file
    
    
if __name__ == '__main__':
    html_data = get_vacancies()
    result = parse_vacancies(html_data)

    write_in_file(result)
