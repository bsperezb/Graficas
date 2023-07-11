from plotGraph import *

# TODO definien en la entrada si es base 100
# TODO Crear for para iterar objetos

graphDetails_nt = {
    'titulo' : "Destruccion de exergia vs NT",
	'titulo_x' : "",
    'titulo_y' : "Exergy Destroyed SORC [%]",
    'nombre_archivo': 'SBCR_SORC_NT.csv',
	'is_base100': True
}
graphDetails_nc = {
    'titulo' : "Destruccion de exergia vs NC",
	'titulo_x' : "",
    'titulo_y' : "Exergy Destroyed SORC [%]",
    'nombre_archivo': 'SBCR_SORC_NC.csv',
	'is_base100': True
}
graphDetails_rc = {
    'titulo' : "Destruccion de exergia vs RC",
	'titulo_x' : "",
    'titulo_y' : "Exergy Destroyed SORC [%]",
    'nombre_archivo': 'SBCR_SORC_RC.csv',
	'is_base100': False
}
graphDetails_t = {
    'titulo' : "Destruccion de exergia vs RC",
	'titulo_x' : "",
    'titulo_y' : "Exergy Destroyed SORC [%]",
    'nombre_archivo': 'SBCR_SORC_T.csv',
	'is_base100': False
}

graphDetails_all = [
	graphDetails_nc,
	graphDetails_nt,
	graphDetails_rc,
	graphDetails_t
]

graphDetails = graphDetails_nt
def main():
	figuras = []
	for graphDetails in graphDetails_all:
		nombre_archivo = graphDetails['nombre_archivo']  # Reemplaza con la ruta y nombre de tu archivo
		df = read_data(nombre_archivo)
		df2 = acumulative_dataFrame(df)
		print(df2)
		# Crear una nueva figura para cada iteración
		fig = plt.figure()

        # Llamar a la función plot_example2 para graficar en la figura actual
		plot_example2(df2, graphDetails)

		figuras.append(fig)
    # Mostrar todas las figuras juntas al final del bucle
	plt.show()


        # Agregar la figura actual a la lista
        # figuras.append(fig)

		# plot_example2(df2, graphDetails)

		# nombre_archivo = graphDetails['nombre_archivo']  # Reemplaza con la ruta y nombre de tu archivo
		# df = read_data(nombre_archivo)
		# df2 = acumulative_dataFrame(df)
		# print(df2)
		# plot_example2(df2, graphDetails)


	# df3 = df2.copy()
	# dfArray = [df2, df3]
	# generate_subplots(dfArray, graphDetails)
	


	# plotExample()

if __name__ == "__main__":
    main()
