from PIL import Image
import numpy as np

# Cargar imagen
img = Image.open('univalle.jpg')

# Convertir imagen en arreglo
img_array_aux = np.asarray(img)
img_array = np.copy(img_array_aux)
nueva_img = img_array

# Funcion para calcular promedio en un arreglo
def prom(arreglo):
	return sum(arreglo) / len(arreglo)


# Funcion para crear nuevo arreglo con el umbral definido
def set_umbral(img_array):
	# Arreglo para almacenar el promedio de cada pixel
	balance_array = []

	for columna in img_array:
		for pixel in columna:
			# Promedio de los colores del pixel
			promedio_pixel = prom(pixel[:3])
			balance_array.append(promedio_pixel)

	# Promedio de color de los pixeles
	balance_img = prom(balance_array)

	# Verificar cada pixel dentro del umbral definido en balance_img
	for columna in nueva_img:
		for pixel in columna:
			# Si el promedio de colores del pixel es mayor al promedio general se da color blanco, si no negro
			if prom(pixel[:3]) > balance_img:
				pixel[0] = 255
				pixel[1] = 255
				pixel[2] = 255
			else:
				pixel[0] = 0
				pixel[1] = 0
				pixel[2] = 0

	return nueva_img



print(nueva_img)
imagen_resultado = Image.fromarray(set_umbral(img_array))
imagen_resultado.save('resultado_bn.png')
