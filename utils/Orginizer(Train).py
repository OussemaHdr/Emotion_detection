import pandas as pd
import os
from tqdm import tqdm
from PIL import Image

pictures_folder = 'C:/Users/Ousse/Desktop/Emotion Detector/Images/Training'
target = 'C:/Users/Ousse/Desktop/Emotion Detector/Images/Train1/'

#for i in range (0,7):
        #os.mkdir('C:/Users/Ousse/Desktop/Emotion Detector/Images/Train1/' + str(i))

for item in os.listdir(pictures_folder):
	base=os.path.basename(item)
	c = os.path.splitext(base)[0][-1]
	picture = Image.open(pictures_folder + '/' + base)
	picture.save('C:/Users/Ousse/Desktop/Emotion Detector/Images/Train1/' + c + '/' + base)