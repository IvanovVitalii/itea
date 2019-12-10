# Show the capital of the country, if the country from the list is in the dictionary
dict_var = {'country1': 'capital1',
            'country2': 'capital2',
            'country3': 'capital3',
            'country4': 'capital4',
            'country5': 'capital5'}
list_country = list(['country1', 'country2', 'country3', 'country5'])
for i in list_country:
    if i in dict_var:
        print(dict_var[i])
