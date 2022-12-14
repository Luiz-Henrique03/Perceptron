import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Perceptron:
    def _init_(self,eta = 0.01,n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    def fit(self,X,y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    def net_input(self,X):
        return np.dot(X,self.w_[1:]) + self.w_[0]
    
df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                 'machine-learning-databases/autos/imports-85.data', header=None)

df.tail()

y = df.iloc[0:100, 4].values
y = np.where(y =='', -1, 1)

X = df.iloc[0:100, [0,2]].values

plt.scatter(X[:50, 0], X[:50, 1], color='red' , marker='o', label='upper left')
plt.scatter(X[50:100,0], X[50:100,1], color='blue', marker='o', label='center')
plt.xlabel('Seguro')
plt.ylabel('Carros')
plt.legend(loc='')
plt.show()