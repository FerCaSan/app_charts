import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        header = next(reader)
        
        data_pop = []
        dict_perc = {}
        for row in reader:            
            iterable = zip(header, row)
            dict_country = {key : value for key, value in iterable 
                            if key == 'Country' or key.__contains__('Population') 
                            and not key.__contains__('Percentage') }
            
            data_pop.append(dict_country)
            dict_perc[row[2]] = row[len(row)-1]
            
            
        return data_pop, dict_perc
 
             
        
   
        