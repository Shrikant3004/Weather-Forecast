import pandas as pd
import numpy as np
import tensorflow
import keras
from keras import Sequential, layers
from keras.layers import Dense

data = pd.read_excel("final1.xlsx")
final_data = data[["Date","TAVG (Degrees Fahrenheit)","TMAX (Degrees Fahrenheit)","TMIN (Degrees Fahrenheit)","PRCP (Inches)"]].copy()
final_data.columns = ["Date", "Tavg", "Tmax", "Tmin", "Prec"]

final_data["Prec"] = final_data["Prec"].fillna(0)
final_data["Tmax"] = final_data["Tmax"].fillna(method="ffill")
final_data["Tmin"] = final_data["Tmin"].fillna(method="ffill")

#adding extra column
final_data["target_Tmax"] = final_data.shift(-1)["Tmax"]
final_data = final_data.iloc[:-1,:].copy()

#train
y_train = final_data["target_Tmax"]
x_train = np.empty((0,5))
#x_train.extend([[3,4]])

#date
date_list = final_data["Date"]

for i in range (len(date_list)) :
   b = final_data["Date"][i]

   if ((b.day!=29 or b.day!=28) and b.month!=2):

    b = b.replace(year=(b.year)-1)

   temp = []
   
   

   index_array = np.where(date_list==b)[0]

   if len(index_array) > 0:
    index = index_array[0]
    temp.extend([final_data["Tmax"][index]])

   else:
    index = -1
    if i>=2:temp.extend([final_data["Tmax"][i-2]])
    else:temp.extend([0])
    
   temp.extend([final_data["Tmax"][i]])
   temp.extend([final_data["Prec"][i]])    
   if i>=1:
     temp.extend([final_data["Tmax"][i-1]])  
     temp.extend([final_data["Prec"][i-1]]) 
   else:
     temp.extend([0])
     temp.extend([0])

   temp = np.array(temp)   
   x_train= np.vstack([x_train,temp])


y_train = np.array(y_train)
print(y_train.shape)
print(x_train.shape)

model = Sequential()
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(1))


from keras.losses import SparseCategoricalCrossentropy 
model.compile(loss= 'mse')

model.fit(x_train,y_train,epochs=7)

















#file_content
