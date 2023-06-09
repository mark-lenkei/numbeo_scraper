headers = [{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/112.0.0.0 Safari/537.36', 'Referrer': 'https://www.google.com/', 
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'},
                         {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Referrer': 'https://www.numbeo.com/', 
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'}]

base_url = "https://www.numbeo.com/cost-of-living/in/"

cities = [{"city":"Amsterdam", "country": "Netherlands", "region": "Europe", "currency":"EUR"},
      {"city":"Athens", "country": "Greece", "region": "Europe", "currency":"EUR"},
      {"city":"Belgrade", "country": "Serbia", "region": "Europe", "currency":"RSD"},
      {"city":"Berlin", "country": "Germany", "region": "Europe", "currency":"EUR"},
      {"city":"Bern", "country": "Switzerland", "region": "Europe", "currency":"CHF"},
      {"city":"Bratislava", "country": "Slovakia", "region": "Europe", "currency":"EUR"},
      {"city":"Brussels", "country": "Belgium", "region": "Europe", "currency":"EUR"},
      {"city":"Bucharest", "country": "Romania", "region": "Europe", "currency":"RON"},
      {"city":"Budapest", "country": "Hungary", "region": "Europe", "currency":"HUF"},
      {"city":"Copenhagen", "country": "Denmark", "region": "Europe", "currency":"DKK"},
      {"city":"Dublin", "country": "Ireland", "region": "Europe", "currency":"EUR"},
      {"city":"Helsinki", "country": "Finland", "region": "Europe",  "currency":"EUR"},
      {"city":"Kiev", "country": "Ukraine", "region": "Europe", "currency":"UAH"},
      {"city":"Lisbon", "country": "Portugal", "region": "Europe", "currency":"EUR"},
      {"city":"Ljubljana", "country": "Slovenia", "region": "Europe", "currency":"EUR"},
      {"city":"London", "country": "United Kingdom", "region": "Europe", "currency":"GBP"},
      {"city":"Luxembourg", "country": "Luxemburg", "region": "Europe", "currency":"EUR"},
      {"city":"Madrid", "country": "Spain", "region": "Europe", "currency":"EUR"},
      {"city":"Minsk", "country": "Belarus", "region": "Europe", "currency":"BYN"},
      {"city":"Moscow", "country": "Russia", "region": "Europe", "currency":"RUB"},
      {"city":"Oslo", "country": "Norway", "region": "Europe", "currency":"NOK"},
      {"city":"Paris", "country": "France", "region": "Europe", "currency":"EUR"},
      {"city":"Podgorica", "country": "Montenegro", "region": "Europe", "currency":"EUR"},
      {"city":"Prague", "country": "Czech Republic", "region": "Europe", "currency":"CZK"},
      {"city":"Milan", "country": "Italy", "region": "Europe",  "currency":"EUR"},
      {"city":"Manchester", "country": "United Kingdom", "region": "Europe",  "currency":"GBP"},
      {"city":"Reykjavik", "country": "Iceland", "region": "Europe", "currency":"ISK"},
      {"city":"Riga", "country": "Latvia", "region": "Europe", "currency":"EUR"},
      {"city":"Rome", "country": "Italy", "region": "Europe", "currency":"EUR"},
      {"city":"Sarajevo", "country": "Bosnia and Herzegovina", "region": "Europe", "currency":"BAM"},
      {"city":"Skopje", "country": "North Macedonia", "region": "Europe", "currency":"MKD"},
      {"city":"Sofia", "country": "Bulgaria", "region": "Europe", "currency":"BGN"},
      {"city":"Stockholm", "country": "Sweden", "region": "Europe", "currency":"SEK"},
      {"city":"Tallinn", "country": "Estonia", "region": "Europe", "currency":"EUR"},
      {"city":"Tirana", "country": "Albania", "region": "Europe", "currency":"ALL"},
      {"city":"Valletta", "country": "Malta", "region": "Europe", "currency":"EUR"},
      {"city":"Vienna", "country": "Austria", "region": "Europe", "currency":"EUR"},
      {"city":"Vilnius", "country": "Lithuania", "region": "Europe", "currency":"EUR"},
      {"city":"Frankfurt", "country": "Germany", "region": "Europe",  "currency":"EUR"},
      {"city":"Munich", "country": "Germany", "region": "Europe",  "currency":"EUR"},
      {"city":"Warsaw", "country": "Poland", "region": "Europe", "currency":"PLN"},
      {"city":"Zagreb", "country": "Croatia", "region": "Europe", "currency":"EUR"},
      {"city":"New-York", "country": "United States", "region": "North America", "currency":"USD"},
      {"city":"Los-Angeles", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Chicago", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Houston", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Philadelphia", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Phoenix", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"San-Antonio", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"San-Diego", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Dallas", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"San-Jose", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Austin", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Jacksonville", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"San-Francisco", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Indianapolis", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Columbus", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Fort-Worth", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Charlotte", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Seattle", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Denver", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Washington", "country": "United States", "region": "North America",  "currency":"USD"},
      {"city":"Mumbai", "country": "India", "region": "Asia",  "currency":"INR"},
      {"city":"Riyadh", "country": "Saudi Arabia", "region": "Middle East",  "currency":"SAR"},
      {"city":"Dubai", "country": "United Arab Emirates", "region": "Middle East",  "currency":"AED"},
      {"city":"Tokyo", "country": "Japan", "region": "Asia",  "currency":"JPY"},
      {"city":"Beijing", "country": "China", "region": "Asia",  "currency":"CNY"},
      {"city":"Istanbul", "country": "Turkey", "region": "Asia",  "currency":"TRY"},
      {"city":"Ankara", "country": "Turkey", "region": "Asia",  "currency":"TRY"},
      {"city":"Saint-Petersburg", "country": "Russia", "region": "Europe",  "currency":"RUB"},
      {"city":"Rio-De-Janeiro", "country": "Brazil", "region": "South America",  "currency":"BRL"},
      {"city":"Bogota", "country": "Colombia", "region": "South America",  "currency":"COP"},
      {"city":"Buenos-Aires", "country": "Argentina", "region": "South America",  "currency":"USD"},
      {"city":"Brasilia", "country": "Brazil", "region": "South America",  "currency":"BRL"},
      {"city":"Sao-Paulo", "country": "Brazil", "region": "South America",  "currency":"BRL"},
      {"city":"Lima", "country": "Peru", "region": "South America",  "currency":"PEN"},
      {"city":"Caracas", "country": "Venezuela", "region": "South America",  "currency":"USD"},
      {"city":"Montreal", "country": "Canada", "region": "North America",  "currency":"CAD"},
      {"city":"Toronto", "country": "Canada", "region": "North America",  "currency":"CAD"},
      {"city":"Cairo-Egypt", "country": "Egypt", "region": "Africa",  "currency":"EGP"},
      {"city":"Tel-Aviv-Yafo", "country": "Israel", "region": "Asia",  "currency":"ILS"},
      {"city":"Sydney", "country": "Australia", "region": "Oceania",  "currency":"AUD"},
      {"city":"Johannesburg", "country": "South Africa", "region": "Africa",  "currency":"ZAR"},
      {"city":"Melbourne", "country": "Australia", "region": "Oceania",  "currency":"AUD"},
      {"city":"Shanghai", "country": "China", "region": "Asia",  "currency":"CNY"},
      {"city":"Bangkok", "country": "Thailand", "region": "Asia",  "currency":"THB"},
      {"city":"Seoul", "country": "South Korea", "region": "Asia",  "currency":"KRW"},
      {"city":"Mexico-City", "country": "Mexico", "region": "North America",  "currency":"MXN"},
      {"city":"Delhi", "country": "India", "region": "Europe",  "currency":"INR"},
      {"city":"Shenzhen", "country": "China", "region": "Asia",  "currency":"CNY"},
      {"city":"Jakarta", "country": "Indonesia", "region": "Asia",  "currency":"IDR"},
      {"city":"Tehran", "country": "Iran", "region": "Asia",  "currency":"USD"},
      {"city":"Kuala-Lumpur", "country": "Malaysia", "region": "Asia",  "currency":"MYR"},
      {"city":"Hong-Kong", "country": "Hong-Kong(China)", "region": "Asia",  "currency":"HKD"},
      {"city":"Singapore", "country": "Singapore", "region": "Asia",  "currency":"SGD"},
      {"city":"Auckland", "country": "New Zealand", "region": "Oceania",  "currency":"NZD"},]

base_column_names = ["date", "city", "country", "region","currency"]

scrape_column_names = ["family_of_four", 
                "single_person_costs",
                "meal_inexp_restaurant",
                "meal_couple_midrange_restaurant",
                "mcmeal_mcdonalds",
                "dom_beer_restaurant",
                "imp_beer_restaurant",
                "cappuccino_restaurant",
                "cola_restaurant",
                "water_restaurant",
                "milk",
                "bread",
                "rice",
                "eggs",
                "local_cheese",
                "chicken_fillets",
                "beef",
                "apples",
                "banana",
                "oranges",
                "tomato",
                "potato",
                "onion",
                "lettuce",
                "water",
                "wine",
                "dom_beer",
                "imp_beer",
                "cigarettes",
                "pub_transp_one_way",
                "pub_transp_monthly",
                "taxi_start",
                "taxi_1km",
                "taxi_1hour",
                "gasoline",
                "vw_golf_or_equ",
                "toyota_corolla_or_equ",
                "utilities",
                "prepaid_mobile_tariff",
                "internet",
                "fitness_club_fee",
                "tennis_court_rent",
                "cinema",
                "private_preschool",
                "international_primary_school",
                "pair_of_jeans",
                "summer_dress",
                "pair_of_nike_shoes",
                "pair_of_leather_shoes",
                "apartment_1bedr_city_center",
                "apartment_1bedr_out_city_center",
                "apartment_3bedr_city_center",
                "apartment_3bedr_out_city_center",
                "price_sq_meter_city_center",
                "price_sq_meter_out_city_center",
                "avg_monthly_net_salary",
                "mortgage_interest_rate",
                "data_entries",
                "unique_contributors"]