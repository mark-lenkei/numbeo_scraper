from write_data import write_data_file
from variables import eu_cities, us_cities



if __name__ == '__main__':
    write_data_file(eu_cities, "eu", "eu_living_expense")
    write_data_file(us_cities, "us", "us_iving_expenses")
