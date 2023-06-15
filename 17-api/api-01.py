import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data = response.json()[0] 
        
        name = country_data['name']['official']
        capital = country_data['capital']
        population = country_data['population']
                
        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        
    else:
        print("Country not found or API error")


def get_countries_by_region(region):
    url = f"https://restcountries.com/v3.1/region/{region}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            name = country['name']['official']
            capital = country['capital']
            population = country['population']
            print(f"Country: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}")
            print("------")
    else:
        print("API error")



def get_countries_by_language(language):
    url = f"https://restcountries.com/v3.1/lang/{language}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            try :
                name = country['name']['official']
                capital = country['capital']
                population = country['population']
                print(f"Country: {name}")
                print(f"Capital: {capital}")
                print(f"Population: {population}")
                print("------")
            except Exception as e :
                pass
    else:
        print("API error")

def get_countries_by_currency(currency):
    url = f"https://restcountries.com/v3.1/currency/{currency}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            try :
                name = country['name']['official']
                capital = country['capital']
                population = country['population']
                print(f"Country: {name}")
                print(f"Capital: {capital}")
                print(f"Population: {population}")
                print("------")
            except Exception as e :
                pass
    else:
        print("API error")


get_country_info("Thailand")
# get_countries_by_region("europe")
# get_countries_by_language("english")
# get_countries_by_currency("EUR")