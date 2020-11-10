## Funciones que utilizaré para limpiar el dataset.
# --------------------

import pandas as pd

def droping_columns(data, lst):
    ''' Función que elimina columnas
        input = dataframe, lista con nombres de columnas a eliminar
        output = draframe sin dichas columnas
    '''
    new_data = data.drop(lst, axis=1)
    return new_data


def looking_for_elements(serie, lst):
    ''' Función que me busca elementos que quiero en la serie y me devuelve
        una lista alfabeticamente ordenada
        input = serie de un dataframa, lista con elementos a buscar
        output = lista con elementos encontrados, ordenada alfabeticamente
    '''    
    new_lst = []
    for s in serie:
        if (s in lst) and (s not in new_lst):
            new_lst.append(s)
    return sorted(new_lst)


def new_index(data):
    ''' Función que reinicia el indice de un dataframe
        input = dataframe con indice desordenado
        output = dataframe con indice ordenado
    '''
    new_data = data.reset_index(drop=True)
    return new_data


def rename_columns(data, dic):
    ''' Función que renombra las columnas
        input = dataframe, diccionario (key=nombre antiguo y value=nombre nuevo)
        ouput = dataframe renombrado
    '''
    data_back_up = data.copy()
    data = data.rename(columns=dic)
    return data