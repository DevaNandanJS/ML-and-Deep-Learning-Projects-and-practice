import numpy as np
from time import process_time

a= np.array([(1,2,3,4,5),(6,7,8,9,10)])
"""
print (a)
print(a.shape)
"""
b= np.array([(1,2,3,4),(5,6,7,8)], dtype=float)

x= np.zeros((4,4))
y= np.ones((4,4))
#print(x+y)

#identity matrix
c= np.eye(4)
#print(c)

b= np.random.random((3,4))
#print(b)

b= np.random.randint(10,100, (3,3))

list_1= [1,2,3,4,5]

np_list= np.asarray(list_1)
#print(np_list.shape, np_list.dtype, type(np_list))



#analysing an array
"""
c= np.random.randint(10,90, (5,5))
print(c.shape)
print(c.ndim)
print(c.size)
print(c.dtype)
"""

#concat in lists
list_2= [1,2,3,4,5,6,7,8,9,10] 
list_3= [11,12,13,14,15,16,17,18,19,20]
list_4= [21,22,23,24,25,26,27,28,29,30]
#print(list_2, list_3)     #they joins two list
#print(list_2 + list_3)


#concat in array
a= np.random.randint(0,10, (2,3))
b= np.random.randint(10,20, (2,3))
"""
print(a)
print(b)

print("adding array", a+b)
print("subtracting array", a-b)
print("multiplying array", a*b)
print("dividing array", a/b)
"""


#or we can do
"""
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

"""

print(a)
a1= np.transpose(a)
print(a1)