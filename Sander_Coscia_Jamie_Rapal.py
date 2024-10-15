import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import classification_report

images = 'crop_part1'
images_array = []
labels = []

for filename in os.listdir(images):
    if filename.endswith('.jpg'):
        age = int(filename.split('_')[0])
        img_path = os.path.join(images, filename)
        img = Image.open(img_path).resize((128, 128)).convert('L')
        img_array = np.array(img).flatten()
        images_array.append(img_array)
        labels.append(age)

