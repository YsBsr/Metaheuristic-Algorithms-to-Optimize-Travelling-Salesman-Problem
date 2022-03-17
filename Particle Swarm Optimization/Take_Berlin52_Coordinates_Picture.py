import matplotlib.pyplot as plt

import random

from Coordinate import Coordinate

import tsplib95

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

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(111)
        

for first, second in zip(coordinates[:-1], coordinates[1:]):
    ax1.plot([first.x, second.x], [first.y, second.y], 'b')

ax1.plot([coordinates[0].x, coordinates[-1].x], [coordinates[0].y, coordinates[-1].y])

for c in coordinates:
    ax1.plot(c.x, c.y, "ro")

plt.show()
