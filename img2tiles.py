from random import randint
import os
import sys
import skimage
from skimage.io import imsave

def getRandomPoint(max):
    return randint(1, int(max))

ROOT_FOLDER = os.path.abspath("/Users/togohi/Desktop/dataset_3")
SIZE = (64, 64)
RANDOM_BY_PHOTO = 50

if not os.path.exists(ROOT_FOLDER):
    print("ROOT Folder {} doesn't exists".format(ROOT_FOLDER))
    sys.exit(0)

OUTPUT_FOLDER = os.path.join(ROOT_FOLDER, "Output")
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

print(ROOT_FOLDER)

for f in os.listdir(ROOT_FOLDER):
    if f.endswith(".ppm"):
        file_path = os.path.join(ROOT_FOLDER, f)
        filename, file_extension = os.path.splitext(f)
        print(filename)
        image = skimage.data.imread(file_path)
        print("Dimensiones: {}".format(image.shape))
        height = image.shape[0]
        width = image.shape[1]

        for i in range(1, RANDOM_BY_PHOTO):
            x_rand = getRandomPoint(width - SIZE[0])
            y_rand = getRandomPoint(height - SIZE[1])
            print("Punto Aleatorio: {}, {}".format(x_rand, y_rand))
            split = image[y_rand:y_rand + SIZE[1], x_rand:x_rand + SIZE[0]]
            imsave(os.path.join(OUTPUT_FOLDER, "{}_split_{}.ppm".format(filename, i)), split)



