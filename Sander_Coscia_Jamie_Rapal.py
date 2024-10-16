import os
import numpy as np
import pandas as pd
from collections import defaultdict
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import classification_report

images = 'crop_part1'
images_array = []
img_sizes = defaultdict(int)
labels = []

for filename in os.listdir(images):
    if filename.endswith('.jpg'):
        age = int(filename.split('_')[0])
        img_path = os.path.join(images, filename)
        img = Image.open(img_path)

        img_sizes[img.size] += 1

        img = img.convert('L')
        img_array = np.array(img).flatten()
        images_array.append(img_array)
        labels.append(age)

        

#--------------------------------------------------------------
#---------------------Task 2: EDA------------------------------
#--------------------------------------------------------------

#Evaluating Distribution of Ages in data
df = pd.DataFrame(labels, columns=['Age'])

plt.figure(figsize=(12,6))
ax = sns.countplot(x='Age', data=df, palette='viridis')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=90)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 12),
                textcoords='offset points', rotation = 90)
    

#Evaluting size of images distribution
size_counts = dict(img_sizes)
sizes_list = list(size_counts.keys())
counts_list = list(size_counts.values())

plt.figure(figsize=(12,6))
plt.bar(range(len(size_counts)), counts_list, tick_label = ['200x200'])
plt.title('Distribution of Image sizes')
plt.xlabel('Image sizes (width, height)')
plt.ylabel('Count')





#Shows all plots
plt.show()
