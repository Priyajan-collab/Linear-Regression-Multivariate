import pandas as pd
from matplotlib import pyplot as pt
import numpy as np

house_data=pd.read_csv("data/train.csv")
y=house_data['price']
x_features=['area','bedrooms','bathrooms','stories','parking']
x=house_data.drop(columns=['price' ,"mainroad","guestroom","hotwaterheating","airconditioning","prefarea","furnishingstatus"])
# print(x[0:])
# pt.style.use("Solaraize2")
fig, ax= pt.subplots(1,5,figsize=(12,3),sharey=True)
w=np.zeros(x.shape[1])
b=np.random.uniform(0,1)
print(w)


def plot_data():
    for i in range(len(x_features)):
      
        ax[i].scatter(x[x_features[i]],y,s=4,c="r")
plot_data()
pt.show()
    
