\import pandas as pd
from matplotlib import pyplot as pt
import numpy as np

house_data=pd.read_csv("data/train.csv")
y=house_data['price']
x_features=['area','bedrooms','bathrooms','stories','parking']
# x=house_data.drop(columns=['price' ,"mainroad","guestroom","hotwaterheating","airconditioning","prefarea","furnishingstatus"])
fig, ax= pt.subplots()

x = house_data[x_features].apply(pd.to_numeric, errors='coerce').fillna(0)
x=np.array(x)

x = (x - np.mean(x, axis=0)) / np.std(x, axis=0) 
y = (y - np.mean(y)) / np.std(y) 
w=np.zeros(x.shape[1]) 
b=np.random.uniform(0,1)
lr=0.001

print(x.shape,w.shape)

class Linear_Regression():
    def __init__(self,x,y,w,b,lr):
        self.x=x;
        self.y=y;
        self.w=w;
        self.b=b;
        self.lr=lr;
    def predict(self):
        self.ys=np.dot(self.x,self.w)+self.b
       
        return self.ys;
    def cost(self):
        squared_error=np.sum((np.array(y)-np.array(self.ys))**2)
        self.result=squared_error/(2*len(self.ys))
        return self.result
    def plot(self):
        ax.set_xlabel("iteration")
        ax.set_ylabel("Cost")
        ax.legend()
    def update_weights_biases(self):
        diff=(np.array(self.y)-np.array(self.ys))
        w_d=(np.dot(diff,self.x))/len(self.ys)
        b_d=np.sum(diff)/len(self.ys)
        self.w+=self.lr*w_d
        self.b+=self.lr*b_d
        
# def plot_data():
#     for i in range(len(x_features)):
      
#         ax[i].scatter(x[x_features[i]],y,s=4,c="r")

    

obj=Linear_Regression(x,y,w,b,lr)

graph_x=[]
graph_y=[]
def train():
    for i in range(1000):
        print("Iteration: ",i)
        
        obj.predict()
        obj.cost()
        print(obj.result)
        obj.update_weights_biases()
        graph_x.append(i)
        graph_y.append(obj.result)

# train()
ax.plot(graph_x,graph_y,c="r")
ax.set_ylabel("cost_error")
ax.set_xlabel("iteration")
# print(graph_y)
# plot_data()
pt.show()
    
