import read_file
import utils
import charts

if __name__ == '__main__':
    
    country = input("Ingrese país a graficar: ")
    data, dict_perc =  read_file.read_csv('./data.csv')
    
    
    
    #To graphic char    
    data_to_graphic = utils.population_country(data, country)
    data_to_graphic_or = sorted(data_to_graphic.items(), key= lambda x: int(x[1]) )
    
    print('DataFinal')
    print(data_to_graphic_or)
    labels , values= zip(*data_to_graphic_or)
    
    print('labels:')
    print(labels)
    print('labels:')
    print(values)
    
    charts.generate_bar_char(labels, values)
    
    #To graphic pie
    
    #if would have in our dictionary data columns percentage, but here we don´t have those columns
    #labels_pie = list(map(lambda x: x['Country'], data) )
    #values_pit = list(map(lambda x: x['World Population Percentage'], data))
    
    labels_pie = dict_perc.keys()
    values_pie = dict_perc.values()
    charts.generate_pie_chart(labels_pie, values_pie)    
    
          