from bs4 import BeautifulSoup


def parse_vacancies(html_data):
    all_info = []

    soup = BeautifulSoup(html_data, 'lxml')

    cards_vacancies = soup.find_all('div', class_='vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter')

    for card in cards_vacancies:
        header = card.find('h2', class_='bloko-header-section-2').text
        company_name = card.find('span', class_='company-info-text--vgvZouLtf8jwBmaD1xgp').text
        city_name = card.find('span', {'data-qa': 'vacancy-serp__vacancy-address_narrow'}).text
        salary_element = card.find('span', class_='fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh')
        salary = salary_element.text.strip() if salary_element else 'не указана'
        link = card.find('a', class_='bloko-link')['href']

        company_name = company_name.replace('\xa0', ' ')

        all_info.append({
            'header': header,
            'company': company_name,
            'city': city_name,
            'link': link,
            'salary': salary
        })

    return all_info
