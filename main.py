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



list_1= [1,2,3,4,5]

np_list= np.asarray(list_1)
print(np_list.shape, np_list.dtype)