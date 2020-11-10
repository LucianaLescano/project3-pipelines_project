## Funciones que utilizaré para limpiar el dataset
## obtenido a partir del Kaggle.
# --------------------

import pandas as pd

def only_usa(data):
    ''' Función que me filtra los paises, quedandose solo con USA
        input = dataframe
        output = nuevo dataframe donde el pais es solo USA
    '''
    new_data = data[data.country.isin(['United States'])]
    return new_data


def new_country(lst):
    ''' Función que me devuelve una lista con muchos US, que luego usaré para hacer
        otro dataframe
        input = nada
        output = lista
    '''
    return ['United States']*len(lst)


def new_deaths(data, lst):
    ''' Función que me suma la columna "deaths" según el año, me devuelve una lista
        que luego utilizaré para hacer otro dataframe
        input = dataframe
        output = lista
    '''
    new_deaths_ = []
    for element in lst:
        year_frame = data[data.year.isin([element])]
        new_deaths_.append(year_frame['deaths'].sum())
    return new_deaths_


def df_from_3lst(list1, list2, list3):
    ''' Función para obtener el dataframe final
        input = tres listas
        output = dataframe
    '''
    df = pd.DataFrame({
        'list1':list1,
        'list2':list2,
        'list3':list3
        })
    return df