## Funciones que utilizaré para limpiar el dataset
## obtenido a partir del API.
# --------------------

import pandas as pd

def only_states(data, condition1, condition2, condition3):
    ''' Función para obtener dataframe final
        input = tres condiciones 
            ouput = dataset final
    '''
    new_data = data[(data.state.isin(condition1) &
                          data.year.isin(condition2) & 
                          data.cause_name.isin(condition3)
                         )]
    return new_data

