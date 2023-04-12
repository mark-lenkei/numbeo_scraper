from variables import base_column_names, scrape_column_names
from datetime import date
from scraper import scrape_city
from time import sleep
import pandas as pd
import random

def write_data_file(cities, file_name):
    data_columns = base_column_names + scrape_column_names
    data = []

    for city in cities:
        city_data = scrape_city(city)
        data.append(city_data)
        sleep(random.uniform(3, 6))
    
    data_df = pd.DataFrame(data, columns=data_columns)
    data_df.to_csv(f"/home/mark/numbeo/data/{file_name}_{date.today().strftime('%Y_%m_%d')}.csv", index=False)

