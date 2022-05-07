input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
#         print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()} = country
        countries[code.casefold()] = country_dict
#
# print(countries)

# chosen = input('Please enter the name of a country: ')
# chosen_copy = chosen.casefold()
# if chosen_copy in countries.keys():                # MY SOLUTION WHICH
#     chlist = list(countries[chosen_copy].values()) # WORKS FINE TOO
#     print(chlist[1])

while True:
    chosen_country = input('Choose a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
    elif chosen_country not in countries:
        print("Please enter a valid one... :")
