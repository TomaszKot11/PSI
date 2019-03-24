import matplotlib.pyplot as plt

class PlotDrawer:

  def __init__(self, cities):
    self.cities = cities
    self.draw_plot()

  def draw_plot(self):
    for i in range(0, len(self.cities) - 1):
      first_city = self.cities[i]
      second_city = self.cities[i + 1]
      plt.plot([first_city[1], second_city[1]], [first_city[2], second_city[2]])
      plt.annotate(str(first_city[0]), (first_city[1], first_city[2]))

    plt.axis([0, 105, 0, 105])
    plt.xlabel('X', fontsize=10)
    plt.ylabel('Y', fontsize=10)
    plt.show()