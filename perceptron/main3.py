import matplotlib.pyplot as plt
import numpy as np
import random
from Perceptron import Perceptron





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

p = np.array([ blue_input_array[0] + red_input_array[0], blue_input_array[1] + red_input_array[1] ])

print(p)

t = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])

# plt.show()

perceptron = Perceptron()

print(len(p[0]))


for i in range(len(p[0])):
  current_point = [ p[0][i], p[1][i] ]
  error_val = perceptron.train(current_point, t[i])

  while error_val != 0.0:
    perceptron.update_weights_and_b(current_point, error_val)
    error_val = perceptron.train(current_point, t[i])

# print(perceptron.weights)
x = np.linspace(-10,10,100)

# print('-------')
# print(- ( (1.0/perceptron.get_weights()[1]) / 1.0/perceptron.get_weights()[0]))
# print((-1)*(1.0/perceptron.get_weights()[1]))
# print('------')

# y1 = - ( (1.0/perceptron.get_weights()[1]) / 1.0/perceptron.get_weights()[0]) * x + (-1)*(1.0/perceptron.get_weights()[1])

slope = -( perceptron.get_weights()[0] / perceptron.get_weights()[2] ) / ( perceptron.get_weights()[0] / perceptron.get_weights()[1] )
intercept = -perceptron.get_weights()[0]/perceptron.get_weights()[2]
y1 = slope * x + intercept
# + slope
plt.plot(x, y1,  label = str(1))
plt.grid(b = True, which = 'both')

plt.show()



