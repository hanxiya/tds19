#%%
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as plot

#%%
import csv

data = {'date':[], 'symbol':[], 'closing_price' : []}
with open('stocks.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        data['date'].append(row["date"])
        data['symbol'].append(row["symbol"])
        data['closing_price'].append(float(row["closing_price"]))
        
data.keys()

#%%
import pandas

data2 = pandas.read_csv('stocks.csv', delimiter='\t',header=None)
print(len(data2))
print(type(data2))

#read_excel
#read_hdf
#read_sql
#read_json
#read_msgpack (experimental)
#read_html
#read_gbq (experimental)
#read_stata
#read_sas
#read_clipboard
#read_pickle

#%%
import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])  #[[]]
A
linalg.inv(A) # inverse of a matrix
b = np.array([[5,6]]) #2D array
b
print(b)
print(A)

b.T#转置
A.T
A*b #not matrix multiplication!
A.dot(b.T) #matrix multiplication

b = np.array([5,6]) #1D array 
b
b.T  #not matrix transpose! 
A.dot(b)  #does not matter for multiplication

#%%求解线性方程组
import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
A
b = np.array([[5],[6]])
b
linalg.inv(A).dot(b) #slow
A.dot(linalg.inv(A).dot(b))-b #check

np.linalg.solve(A,b) #fast
A.dot(np.linalg.solve(A,b))-b #check

#%%行列式
import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
linalg.det(A)

#%%最小二乘和广义逆
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

c1, c2 = 5.0, 2.0
i = np.r_[1:11]
xi = 0.1*i
yi = c1*np.exp(-xi) + c2*xi
zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi))

A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
c, resid, rank, sigma = linalg.lstsq(A, zi) #系数解，残差，rank，系数标准差

xi2 = np.r_[0.1:1.0:100j] #画图辅助点
yi2 = c[0]*np.exp(-xi2) + c[1]*xi2 #拟合直线

plt.plot(xi,zi,'x',xi2,yi2)
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Data fitting with linalg.lstsq')
plt.show()

#%%作业：矩阵运算
from numpy import *
import numpy as np
A = np.array([[2,5,1],[9,12,3],[16,24,18]])
A = mat(A)
B = np.array([[5,8,19],[26,15,12],[31,8,7]])
B = mat(B)
C = np.array([[1,2,3],[4,5,6],[7,8,9]])
C = mat(C)
#加法
A+B
#结合律
(A+B)+C == A+(B+C)
#交换律
A+B == B+A
#零矩阵
Z = mat(zeros((3,3)))
Z
A+Z == A
#

#%%
mat(ones((2,4))) #1矩阵
mat(random.randint(10,size=(3,3))) #1~10随机整数，3*3矩阵
mat(eye(2,2,dtype=int))#对角阵 整数
a1=[1,2,3]
mat(diag(a1))#对角阵

#%% 改写
from numpy import *
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

c1, c2 = 5.0, 2.0
i = np.r_[1:11]
i = mat(i).T
xi = 0.1*i
yi = c1*exp(-xi) + c2*xi
zi = yi + 0.05 * max(yi)[0,0] * mat(np.random.randn(len(yi))).T
A = hstack((exp(-xi),xi))
c, resid, rank, sigma = linalg.lstsq(A, zi,rcond=None) #系数解，残差，rank，系数标准差

xi2 = np.r_[0.1:1.0:100j] #画图辅助点
yi2 = c[0,0]*exp(-xi2) + c[1,0]*xi2 #拟合直线

plt.plot(xi,zi,'x',xi2,yi2)
plt.axis([0,1.1,3.0,5.5])
plt.xlabel('$x_i$')
plt.title('Data fitting with linalg.lstsq')
plt.show()
























