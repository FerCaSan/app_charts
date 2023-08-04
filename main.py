import read_file
import utils
import charts
import pandas as pd

def data_preparation_dict_list():
    
    #Function to prepare data using dictionaries and list
    
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
    
def data_preparation_pandas():
    #Function to prepare data using Pandas

    #To graphic char     
    country = input("Ingrese país a graficar: ")
    df = pd.read_csv('./data.csv')
    
    df_country = df[df['Country'] == country ]
    df_country.drop(columns=['Country', 'Rank', 'CCA3', 'Capital'
                             , 'Continent'
                             , 'Area (km²)', 'Density (per km²)'
                             , 'Growth Rate', 'World Population Percentage']
                    , inplace=True)
    
    
    label_popu_per_year = df_country.columns
    values_popu_per_year = df_country.values.flatten()
    #Output with flatten: [[51874024 50930662 ....]] -->Array two-dimension
    #Output without flatten: [51874024 50930662 ....] -->Array one-dimension
    
    print(values_popu_per_year)
    charts.generate_bar_char(country,label_popu_per_year, values_popu_per_year)
    
    #To graphic pie
    df_percentage = df[df['Continent'] == 'South America']
    countries = df_percentage['Country'].values
    percentage = df_percentage['World Population Percentage'].values
    
    charts.generate_pie_chart(countries, percentage) 

def run():
    #data_preparation_dict_list()
    data_preparation_pandas()
             
    
if __name__ == '__main__':
    run()
  
    
          