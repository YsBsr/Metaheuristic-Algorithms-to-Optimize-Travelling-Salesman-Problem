import matplotlib.pyplot as plt

import random

from Coordinate import Coordinate

import tsplib95

import numpy

"""

Berlin52 dosyasında 52 tane konumun kordinatlarını bulunmaktadır
tsplib95 kütüphanesini kullanarak bu konumları alacağım.

tsplib95 kütüphanesi okuduğu bu koordinatları(konumları)
bir dictionary veri yapısında tutuyor,
bu yapıdaki koordinatları alıp Coordinates class'ının nesnelerinden
oluşan bir listeye çevireceğim.

"""

coordinates = []
#koordinatlarımızı Coordinate class'ı nesneleri ile tutacağımız liste.

problem = tsplib95.load('berlin52.tsp')
#berlin52.tsp dosyasını tsplib95 kütüphanesi ile okuyoruz.

nodes = problem.node_coords.values()
#tsplib95 kütüphanesi berlin95.tsp dosyasındaki konumları okuduktan sonra
#bu konumları bir dictionary veri yapısında tutar (key-value çiftleri ile)
#bu dictionarydeki valueler bizim 52 tane konumuzun birer birer (x, y) koordinatlarıdır.

for x, y in problem.node_coords.values():
        coordinates.append(Coordinate(x, y))
        #En yukarda import ettiğim Coordinate class'ını kullanarak
        #coordinates listemi berlin52.tsp dosyasının içindeki koordinatlar(konumlar)
        #ile dolduruyorum.

if __name__ == '__main__':

  costs = []

  temperatures = []

  cost0 = Coordinate.get_total_distance(coordinates)

  length = len(coordinates)

  T = 100
  factor = 0.20

  costs_total = 0

  for i in range(1000):
    print(i, "Cost", cost0)
    costs.append(cost0)
    costs_total += cost0
    temperatures.append(T)

    T = T * factor

    for j in range(100):
      r1, r2 = numpy.random.randint(0, length, size = 2)

      temporary = coordinates[r1]
      coordinates[r1] = coordinates[r2]
      coordinates[r2] = temporary

      cost1 = Coordinate.get_total_distance(coordinates)

      if (cost1 < cost0):
        cost0 = cost1
      else:
        r = numpy.random.uniform()

        if r < numpy.exp((cost0 - cost1) / T):
          cost0 = cost1
        else:
          temporary = coordinates[r1]
          coordinates[r1] = coordinates[r2]
          coordinates[r2] = temporary

  cost_average = costs_total / 1000

  print("cost average: ", cost_average)

  fig = plt.figure(figsize=(10,5))

  ax1 = fig.add_subplot(111)

  ax1.plot(costs)

  plt.show()

  


















  
