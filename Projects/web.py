# from crypt import methods
# from distutils.log import debug
import pathlib
from urllib import response
from app import app
from flask import Flask, render_template, request,redirect, url_for,flash
from werkzeug.utils import secure_filename
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
from tensorflow.keras.preprocessing import image
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


import sys
sys.path.append('..')


    



@app.route('/')
def home():
    return render_template('detection.html')




@app.route('/upload_video', methods=['POST'])
def upload_video():


    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        y=('static/uploads/'+ filename)
        print(y)
        model=load_model("heart.h5")
        def testing_image(y):
            test_image = image.load_img(y, target_size = (224, 224))
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
            print(prediction)

        x=(testing_image(y))
        


        return render_template('detection.html',out=x,data=y)
        print(data)
        


        


if __name__=="__main__":
    app.run(debug= True)
