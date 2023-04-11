from variables import headers, base_url
from bs4 import BeautifulSoup
from datetime import date
import numpy as np
import requests
import re



def scrape_city(city):
    # Making request
    url = base_url+city["city"]
    source = requests.get(url, headers=headers)
    soup = BeautifulSoup(source.text, 'html.parser')

    # Finding all the necessary parts in html
    emp_numbers_html = soup.find_all("span", {"class": "emp_number"})
    avg_prices_html = soup.find_all("span", {"class": "first_currency"})
    contributors_html = soup.find("div", {"class": "align_like_price_table"})
    
    # Getting data out of html
    family_of_four = get_emp_data(emp_numbers_html[0])
    single_person_monthly_costs = get_emp_data(emp_numbers_html[1])
    avg_prices = [get_data(float_number) for float_number in avg_prices_html]
    
    if contributors_html:
        contributors = re.findall(r'\d+', contributors_html.text)
        entries = contributors[0]
        unique_contributors = contributors[2]
    else:
        entries = None
        unique_contributors = None

    return [date.today().strftime('%Y-%m-%d'), city["city"], city["currency"], family_of_four,
            single_person_monthly_costs] + avg_prices + [entries, unique_contributors]


def get_data(html):
    text = html.text
    if text:
        number = string_to_float(text)
        return number

    return None

def get_emp_data(html):
    text = html.text
    text = text.split("(")

    if len(text) == 1:
        return string_to_float(text[0])

    return string_to_float(text[1])


def string_to_float(text):
    string = text
    string = string.replace(",", "")
    number = np.float32(re.search(r"\d+\.\d", string).group())
    return number

