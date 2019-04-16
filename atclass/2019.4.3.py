#%%
input #交互
#匿名函数 return lambda x:x+n

#%%

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
MyClass()
MyClass.i
MyClass.f(1)

MyClass.i = 3  #更改属性值
MyClass.i

MyClass.x = 1  #根据需要添加定义中没有的属性
MyClass.x

class Complex:
    def __init__(self, realpart, imagpart):  #注意：特殊方法“__init__”前后分别有两个下划线
        self.r = realpart
        self.i = imagpart
    
x = Complex(3.0, -4.5)
x.r, x.i

#%%
a = [1,2,3]
type(a)

a.append(4)  #往list中追加元素到末尾
a

a.insert(2,'a')  #把元素插入到指定的位置
a

a.remove('a')  #移除列表中第一个指定元素
a

b = [4,5,6]
a.extend(b)  #将两个列表合并
a

#%%
a = [1,2,3,4]
b = a 
print(a)
print(b)

a.append(100)
print(a)
print(b)

#%%
a = [1,2,3,4]
b = a.copy()
print(a)
print(b)

a.append(100)
print(a)
print(b)

#%%
a = [1,2,3]
b = [4,5,6]
a + b

#%%
f = lambda x:x+1
f(10)

def make_incrementor(n):
    return lambda x,y: x + y + n  #返回一个函数
g = make_incrementor(42)
g(3,2)
 
#%%
squares = [] # the usual way
for x in range(10):
    squares.append(x**2)
squares

squares = [x**2 for x in range(10)]
squares

import math
squares = [math.exp(x) for x in range(10)]
squares


import math
squares = list(map(lambda x: math.exp(x), range(10))) #map=apply
squares

#%% list
def matrixTriIndex(n, diag = True, lower = True):
    if lower:
        if diag:
            return([(i+1,j+1)for i in range(n) for j in range(n) if i>=j])
        else:
            return([(i+1,j+1)for i in range(n) for j in range(n) if i>j])
    else:  
        if diag:
            return([(i+1,j+1)for i in range(n) for j in range(n) if i<=j])
        else:
            return([(i+1,j+1)for i in range(n) for j in range(n) if i<j])
         
matrixTriIndex(5,False,True)
matrixTriIndex(5,True,False)

#%%
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
matrix
[[row[0] for row in matrix] for i in range(4)]

#%% dictionary
{x: x**2 for x in (2, 4, 6, 8)}

#%%
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

#%%
import sys
help(sys.stdin)
for line in sys.stdin




