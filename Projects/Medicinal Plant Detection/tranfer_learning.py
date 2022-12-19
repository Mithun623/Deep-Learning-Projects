

import cv2
from glob import glob
import pathlib 
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Conv3D,MaxPool3D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.models import load_model

model=load_model("heart.h5")



from tensorflow.keras.preprocessing import image
# testing the model
def testing_image(image_directory):
    test_image = image.load_img(image_directory, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    result = model.predict(test_image)
    print(result)
    if np.argmax(result)  == 0:        
      prediction = 'Betel'
    elif np.argmax(result)  == 1:
      prediction = 'Curry'
    elif np.argmax(result) ==2: 
      prediction = 'Guava'
    elif np.argmax(result) ==3:
      prediction = 'Jackfruit'
    elif np.argmax(result) == 4:
      prediction = 'Lemon'
    elif np.argmax(result) == 5:
      prediction = 'Mango'
    elif np.argmax(result) ==6:
      prediction = 'Mint'
    elif np.argmax(result) == 7:
      prediction = 'Neem'
    elif np.argmax(result) == 8:
      prediction= 'Sandalwood'
    elif np.argmax(result) == 9:
      prediction ='Tulsi'
    return prediction

print(testing_image(r'C:\Users\admin\Desktop\New folder\Data\Artocarpus Heterophyllus (Jackfruit)\AH-S-001.jpg'))

