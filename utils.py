def population_country(data,country):
    population_by_year = list(filter(lambda population: population['Country'] == country, data ))
    
    print('Population by year')
    print(population_by_year[0])
    
    del population_by_year[0]['Country']
    
    print('Population by yea with del Country')
    print(population_by_year[0])
    
    population_by_year = [{k.replace('Population','') : v for k, v in d.items()} for d in population_by_year]
    
    print('Population by after dict')
    print(population_by_year[0])
    
    population_by_year_d = population_by_year.pop(0)
    
    print('population_by_year_d')
    print(population_by_year_d)
    
    return population_by_year_d