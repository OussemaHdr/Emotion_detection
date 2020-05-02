import os
import pandas as pd
import numpy as np
import scipy.misc
from tqdm import tqdm

w = 48
h = 48
image = np.zeros((h, w), dtype=np.uint8)
n = 0

csvfile = "fer2013.csv"
image_folder  = "Images"

data = pd.read_csv(csvfile, delimiter =',')

for item in tqdm(range(0, data.shape[0])):
    emotion = data['emotion'][item]
    pixels = data['pixels'][item].split()
    pixels_array = np.asarray(pixels, dtype=np.int)
    image = pixels_array.reshape(w, h)
    stacked_image = np.dstack((image,) * 3)
    target =  image_folder + "/" + str(n)+'_'+str(emotion)+'.jpg'
    scipy.misc.imsave(target, stacked_image)
    n += 1
    print('Processed {} images'.format(n))
