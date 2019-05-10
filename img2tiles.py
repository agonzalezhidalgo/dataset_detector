from random import randint
import os
import sys
import skimage
from skimage.io import imsave

# Genera un número aleatorio entre 1 y max.
def getRandomPoint(max):
    return randint(1, int(max))

##### Constantes para el funcionamiento del programa
# Carpeta donde se encuentran las imágenes completas
ROOT_FOLDER = os.path.abspath("/Users/togohi/Desktop/dataset_3")
# Dimensiones de los extractos a generar
SIZE = (64, 64)
# Número de extractos aleatorios que se generarán por foto
RANDOM_BY_PHOTO = 50

# Se comprueba que existe la carpeta de entrada
if not os.path.exists(ROOT_FOLDER):
    print("ROOT Folder {} doesn't exists".format(ROOT_FOLDER))
    sys.exit(0)

# Se comprueba que existe la carpeta de salida (sino se crea)
OUTPUT_FOLDER = os.path.join(ROOT_FOLDER, "Output")
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

# Se inicia una iteración por cada fichero de la carpeta de entrada
for f in os.listdir(ROOT_FOLDER):
    # Solo se tiene en cuenta las imágenes con extensión .ppm
    if f.endswith(".ppm"):
        file_path = os.path.join(ROOT_FOLDER, f)
        filename, file_extension = os.path.splitext(f)
        print(filename)

        # Cargamos la fotografía
        image = skimage.data.imread(file_path)
        print("Dimensiones: {}".format(image.shape))

        # Se extraen las dimensiones originales de la fotográfia.
        height = image.shape[0]
        width = image.shape[1]

        # Se generar de 1 a N extracciones aleatorias
        for i in range(1, RANDOM_BY_PHOTO):
            x_rand = getRandomPoint(width - SIZE[0])
            y_rand = getRandomPoint(height - SIZE[1])
            print("Punto Aleatorio: {}, {}".format(x_rand, y_rand))
            split = image[y_rand:y_rand + SIZE[1], x_rand:x_rand + SIZE[0]]
            # Se guarda en disco el extracto.
            imsave(os.path.join(OUTPUT_FOLDER, "{}_split_{}.ppm".format(filename, i)), split)


            