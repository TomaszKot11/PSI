import matplotlib.pyplot as plt
import time
import datetime

#TODO: draw distances!
#TODO: test if algorithm gives proper results!
class PlotDrawer:

  def __init__(self, city_storage = None, cities = None, times = None, title=''):
    self.title = title
    self.city_storage = city_storage
    if not(cities == None):
      self.cities = cities
      self.draw_cities_plot()
    elif not(times == None):
      self.times = times
      self.draw_time_plot()

  def draw_cities_plot(self):
    all_cities = self.city_storage.cities
    for i in range(0, self.city_storage.number_cities):
      first_city = all_cities[self.cities[i]]
      second_city = all_cities[self.cities[i + 1]]
      plt.plot([first_city[1], second_city[1]], [first_city[2], second_city[2]])
      plt.annotate(str(first_city[0]), (first_city[1], first_city[2]))

    plt.axis([0, 105, 0, 105])
    plt.xlabel('X', fontsize=10)
    plt.ylabel('Y', fontsize=10)
    plt.suptitle(self.title)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    plt.savefig(st+'plot.png')
    plt.show()

  def draw_time_plot(self):
    no_x_values = len(self.times)
    max_value = max(self.times)
    plt.axis([0, no_x_values + 1, 0, max_value + max_value / 4.0 ])
    for i in range(0, no_x_values):
      plt.bar(i, self.times[i], width=0.25, align='edge')
    plt.suptitle(self.title)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    plt.savefig(st + 'table.png')
    plt.show()