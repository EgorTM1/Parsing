import requests
from fake_useragent import UserAgent


ua = UserAgent()
    
headers={'User-Agent': ua.random}

def get_vacancies():
    url = 'https://spb.hh.ru/search/vacancy?text=Python+django+flask&salary=&ored_clusters=true&area=1&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'

    response = requests.get(url, headers=headers)

    return response.text
