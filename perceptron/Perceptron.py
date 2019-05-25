import random
import numpy as np

class Perceptron:

  def __init__(self):
    self.weights = np.array([random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)])
    self.b = random.uniform(0.0, 1.0)


  def activation_function(self, a):
    if a >= 0:
      return 1
    elif a < 0:
      return -1


  # inputs are x1, x2
  def train(self, inputs, t_desired):
    activation_value_for_pair = self.feed_forward(inputs)

    print('-----')
    # print(inputs[0])
    # print(inputs[1])
    print(activation_value_for_pair)
    print(t_desired)
    print('-----')



    error = t_desired - activation_value_for_pair

    return error

  def update_weights_and_b(self, inputs, error):
    self.weights = self.weights + np.multiply(error, np.array([ inputs[0], inputs[1] ]))
    self.b = self.b + error


  # calculates the activation function for giuven x1 x2
  def feed_forward(self, p):
    # nie wiem czy to dobrze?
    a = (self.weights[0] + self.weights[1])*(p[0]+p[1]) + self.b

    return self.activation_function(a)

  def get_weights(self):
    return self.weights