import pandas as pd
from matplotlib import pyplot as pt

house_data=pd.read_csv("data/train.csv")
y=house_data['price']
x_features=['area','bedrooms','bathrooms','stories','parking']
# pt.style.use("Solaraize2")
fig, ax= pt.subplots(1,5,figsize=(12,3),sharey=True)

def plot_data():
    for i in range(len(x_features)):
        print(i)
        ax[i].scatter(house_data[x_features[i]],y,s=4,c="r")
plot_data()
pt.show()
    
