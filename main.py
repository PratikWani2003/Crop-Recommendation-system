import pandas as pd
import numpy as np
import seaborn as sns
crop= pd.read_csv(r"C:\Users\prati\Desktop\crop reccomendation system\Dataset\archive (1)\Crop_recommendation.csv")
crop.head()
# print(crop.head()) #to print the top som entries
# print(crop.shape) #to know the shape of data-set
#print(crop.info()) #to know the type of data and the size
#print(crop.isnull().sum()) #to find the numm bvalues in a row
print(crop.duplicated().sum()) # to find duplicates

correlation = crp.corr()
