# print(  " " + "hola" )
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Circle
import pandas as pd

def convert_colors(colorsRGB):
    colorsHex = []
    for color in colorsRGB:
        r, g, b = color
        r /= 255
        g /= 255
        b /= 255
        colorHex = mcolors.to_hex((r, g, b))
        colorsHex.append(colorHex)
    return colorsHex


def acumulative_dataFrame(df):
    x = df.iloc[:, 0]  # Primera columna del dataframe como datos para el eje x
    y = df.iloc[:, 1:]  # Resto de columnas del dataframe como datos para el eje y

    result_df = pd.DataFrame({'x': x})  # Dataframe resultante con la columna 'x' original
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Calcular las columnas adicionales
    for col in y.columns:
        cumulative_col = y.loc[:, :col].sum(axis=1)  # Suma acumulativa de las columnas hasta 'col'
        result_df[col ] = cumulative_col

    return result_df

def read_data (nombre_archivo):
	df = pd.read_csv(nombre_archivo)
	pd.set_option('display.max_columns', None)
	pd.set_option('display.max_rows', None)
    # Devolver el DataFrame
	return df

def plot_example2(df, graphDetails):
    # plt.figure()
    x = df.iloc[:, 0]  # Primera columna del dataframe como datos para el eje x
    y = df.iloc[:, 1:]  # Resto de columnas del dataframe como datos para el eje y
    
    if (graphDetails['is_base100']):
        x = x.apply(lambda x: x * 100)  # Cambiar el tamaño de los ejes a base de 100
    colorsRGB = [
        (195, 155, 211 ), 
        (127, 179, 213 ), 
        (217, 136, 128 ), 
        (247, 220, 111 ), 
        (118, 215, 196), 
        (229, 152, 102), 
        (191, 201, 202 )]
    colorsRGB = convert_colors(colorsRGB)

    # Graficar áreas
    # columnName = [  'Campo solar', 'Calentador/Recalentador', '(HTR,Col,Eva,Rec,LTR, Con)', '(T1,T2,T3)' ,'(C1,C2, P1)' ]
    x1 = 0
    # y_cumulative = pd.Series(0, index=x.index)
    columnName = y.columns[::-1]  # Inversión
    for column in columnName:
        if column == 'Total': 
            continue
        # y_cumulative += y[column]  # Suma acumulada de la columna actual y las anteriores
        x1 = x1 + 1
        print(column)
        # import ipdb; ipdb.set_trace()
        plt.fill_between(x, 0,y[column], label=column, color=colorsRGB[x1], hatch='.')

    plt.title(graphDetails['titulo'])
    # plt.legend(loc="upper left")
    plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    plt.ylabel(graphDetails['titulo_y'])  # Título del eje Y
    plt.xlabel(graphDetails['titulo_x']) # Titulo en x
    plt.subplots_adjust(right=0.7)
	# Initial points
    plt.xlim(x.iloc[0], x.iloc[-1])
    y = y.drop('Total', axis=1) # delete Total columns
    plt.ylim(0, y.max().max())

 # Agregar marcadores de texto en la gráfica
    # markers = [
    #     {'x': 0.70, 'y': 10, 'text': '1'},
    #     {'x': 0.70, 'y': 30, 'text': '2'},
    #     {'x': 0.70, 'y': 60, 'text': '3'}
    # ]
#     for marker in markers:
#         plt.text(marker['x'], marker['y'], marker['text'], ha='center', va='bottom')

    # for marker in markers:
    #     ax = plt.gca()
    #     circle = Circle((marker['x'], marker['y']), 2, color='gray', fill=True)
    #     ax.add_patch(circle)
    #     plt.annotate(marker['text'], (marker['x'], marker['y']), color='white', va='center', ha='center', weight='bold')
# 	# Show Graph
    # plt.show()

def generate_subplots(dataframes, graphDetails):
    num_plots = len(dataframes)

    # Configurar la figura y los subplots
    fig, axes = plt.subplots(1, num_plots, figsize=(num_plots * 6, 6))

    # Iterar sobre los dataframes y generar las gráficas en los subplots correspondientes
    for i, df in enumerate(dataframes):
        ax = axes[i]
        plot_example2(df, graphDetails)
        ax.set_title('Gráfica {}'.format(i + 1))

    # Compartir el título del eje y en todos los subplots
    fig.text(0.04, 0.5, graphDetails['titulo_y'], va='center', rotation='vertical')

    # Ajustar los subplots
    plt.tight_layout()

    # Mostrar las gráficas
    plt.show()