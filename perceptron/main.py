import numpy as np
import random
# import matplotlib
# matplotlib.use('agg')
# %matplotlib inline
import matplotlib.pyplot as plt

# p = np.array([[1,-25],[2,-10],[-8,20],[-9,-10],[7,10], [-5, 1],[15,-1], [10,-4]])
# test = np.array([[-5,-25],[-3,-10],[8,20],[2,-13],[5,11], [10, 3],[15,1]])
p = np.array([[-6, -25], [-2, -10], [1, -10], [4, -16], [5, 9], [-9, -10], [-8, 20], [-6, -5], [2, 20], [4, 25]])
# t= np.array([1,1,0,1,0,0,1,1])

blue_input_array = [
  [-6, -2, 1, 4, 5],
  [-25, -10, -10, -16, 9]
]

red_input_array = [
  [-9, -8, -6, 2, 4],
  [-10, 20, -5, 20, 25]
]

plt.plot( red_input_array[0], red_input_array[1] , 'ro')
plt.plot( blue_input_array[0], blue_input_array[1] , 'bo')

t = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
w=np.array([random.random(),random.random()])
b=[random.random()]

def funkcja_aktywizacji(pCopy,t,w,b,i):
  a=(w[0]+w[1])*(pCopy[i][0]+pCopy[i][1])+b
  if a>0:
    pCopy[i][1]=1
  else:
    pCopy[i][1]=0
  e = t[i]-pCopy[i][1]
  return e

def perceptron(p,t,w,b):
  p1=p.copy()
  for i in range(0,p1.shape[0]):
    a=(w[0]+w[1])*(p1[i][0]+p1[i][1])+b

    if a>0:
      p1[i][1]=1
    else:
      p1[i][1]=0

    e=t[i]-p1[i][1]

    while e!=0.0:
      w[0]=w[0]+e*p1[i][0]+e*p1[i][0]
      w[1]=w[1]+e*p1[i][1]+e*p1[i][1]
      b=b+e
      e=funkcja_aktywizacji(p1,t,w,b,i)

  return(w,b)


w,b=perceptron(p,t,w,b)

x = np.linspace(-10,10,100)
y1 = - ( (1/w[1]) / 1/w[0]) * x + (-1)*(1/w[1])
counter = 0
plt.plot(x, y1,  label = str(counter))
counter = counter + 1

plt.show()
# testVal = []
# for i in range(0,test.shape[0]):
#     #przemnożenie elementów przez wagi
#   a=(w[0]+w[1])*(test[i][0]+test[i][1])+b

#   if a>0:
#       testVal.append(1)
#   else:
#       testVal.append(0)

# print(p)
# for i in range(len(test)):
#   c = "green"
#   if(testVal[i] == 0):
#     c = "yellow"
#   plt.scatter(test[i][0], test[i][1], color=c, s=10)

# for i in range(len(p)):
#   c = "red"
#   if(t[i] == 0):
#     c = "blue"
#   plt.scatter(p[i][0], p[i][1], color=c, s=10)
#   # plt.annotate(t[i], (p[i][0] + 0.1,p[i][1]+ 0.1))
# plt.savefig('test')