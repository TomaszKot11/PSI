import matplotlib.pyplot as plt
import numpy as np
import random


# number of points
n = 5

blue_input_array = [
  [-6, -2, 1, 4, 5],
  [-25, -10, -10, -16, 9]
]

red_input_array = [
  [-9, -8, -6, 2, 4],
  [-10, 20, -5, 20, 25]
]


t = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# blue_input_array = [
#   [1, 2, -8, -9, 7, -5, 15, 10],
#   [-25, -10, 20, -10, 10, 1, -1, -4]
# ]

# red_input_array = [
#   [],
#   []
# ]

p = [
  blue_input_array[0] + red_input_array[0],
  blue_input_array[1] + red_input_array[1]
]

# t = [1,1,0,1,0, 1,1,0,1,0]

weights = [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)]
b = random.uniform(0.0, 1.0)


plt.plot( red_input_array[0], red_input_array[1] , 'ro')
plt.plot( blue_input_array[0], blue_input_array[1] , 'bo')

def funkcja_aktywacji(a):
  if a >= 0:
    return 1
  elif a < 0:
    return -1

# def perceptron(p, w, b, t):
#   # multiply the weigths by the input matrix
#   p1 = p.copy()

a = np.matmul(np.array(weights), np.array(p))
# add the b
a = a + b
y = [ funkcja_aktywacji(a_i) for a_i in a ]
# e = t - y
e = np.subtract(t, y)

counter = 0

if any( e_i != 0.0 for e_i in e):
  for idx, e_i in enumerate(e):
    if e_i != 0.0:
      w_new = weights + (np.multiply(e_i,  np.transpose([ p[0][idx], p[1][idx] ])))
      weigths = w_new
      b_new = b + e_i
      x = np.linspace(-10,10,100)
      y1 = - ( (1/weigths[1]) / 1/weights[0]) * x + (-1)*(1/weights[1])
      plt.plot(x, y1,  label = str(counter))
      counter = counter + 1
      # print('-------')
      # print(w_new)
      # print('-------')
      # # print(result[idx])
      # print('-------')
      a = np.matmul(w_new, np.array([ p[0][idx], p[1][idx] ]))
      activation_fun_val = funkcja_aktywacji(a)
      y[idx] = activation_fun_val
      e[idx] = t[idx] - y[idx]

# print(y)
# print(p)
print(a)
print(w_new)
print(b)

# # draw the plot with result and dots
# plt.plot( red_input_array[0], red_input_array[1] , 'ro')
# plt.plot( blue_input_array[0], blue_input_array[1] , 'bo')
plt.legend(loc='upper left')
plt.show()
