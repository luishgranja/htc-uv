from PIL import Image
import math

# Cargar imagen
img = Image.open('univalle.jpg')

#Obtener alto y ancho de la imagen
width, height = img.size

# Variable tipo Image en la que se guardan los datos finales
nueva_img = Image.new("RGB", (width, height), "white")

for x in range(1, width-1):
	for y in range(1, height-1):

		# Inicializar los Gradientes Gx Gy para cada pixel
		Gx = 0
		Gy = 0

		# top left pixel
		p = img.getpixel((x-1, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		# intensidad varia de 0 a 765 (255 * 3)
		intensidad = r + g + b

		# acumular los valores en Gx, y Gy
		Gx += -intensidad
		Gy += -intensidad

		# remaining left column
		p = img.getpixel((x-1, y))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += -2 * (r + g + b)

		p = img.getpixel((x-1, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += -(r + g + b)
		Gy += (r + g + b)

		# middle pixels
		p = img.getpixel((x, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gy += -2 * (r + g + b)

		p = img.getpixel((x, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gy += 2 * (r + g + b)

		# right column
		p = img.getpixel((x+1, y-1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += (r + g + b)
		Gy += -(r + g + b)

		p = img.getpixel((x+1, y))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += 2 * (r + g + b)

		p = img.getpixel((x+1, y+1))
		r = p[0]
		g = p[1]
		b = p[2]

		Gx += (r + g + b)
		Gy += (r + g + b)

		# calculate the length of the gradient (Pythagorean theorem)
		length = math.sqrt((Gx * Gx) + (Gy * Gy))

		# normalise the length of gradient to the range 0 to 255
		length = length / 4328 * 255

		length = int(length)

		# draw the length in the edge image
		nueva_img.putpixel((x,y),(length,length,length))

nueva_img.save('resultado_sobel.png')