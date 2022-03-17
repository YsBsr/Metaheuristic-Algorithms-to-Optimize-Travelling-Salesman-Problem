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

cost0 = 0 #ilk çözümümüzün değişkenini burada tanımladım ve default değer verdim.
cost0 = Coordinate.get_total_distance(coordinates)

percent40save = 0

population = []

pop_size = 50

def copy_array(array):

    new_array= []

    for i in array:
        new_array.append(i)

    return new_array

def create_individual():

    individual = []

    length = len(coordinates)
    individual = [coordinates[random.randint(0, length - 1)] for i in range(length)]
    
    return individual

    
def create_population(population_size):
    return [create_individual() for i in range(population_size)]
    

    
def fitness(member):
    
    total_costs = 0
    
    total_costs += Coordinate.get_total_distance(member)

    return total_costs



def mutate(member):
    new_member = copy_array(member)


    length = len(new_member)

    r1 = random.randint(0, length - 1)
    r2 = random.randint(0, length - 1)
    
    temporary = new_member[r1]
    new_member[r1] = new_member[r2]
    new_member[r1] = temporary

    return new_member


def crossover(population):
    new_pop = copy_array(population)
        
    parent_elitizm = 0.2

    parent_length = int(parent_elitizm * len(new_pop))

    parents = new_pop[:parent_length]
    noparents = new_pop[parent_length:]

    children = []

    desired_length = len(new_pop) - len(parents)

    while len(children) < desired_length:
        p1 = mutate(parents[random.randint(0, len(parents) - 1)]) 
        p2 = mutate(parents[random.randint(0, len(parents) - 1)])
        #ebevenyler arasından iki kişi seçtik
        half = int(len(p1) / 2)

        child = p1[:half] + p2[half:]
        children.append(child)

    parents.extend(children)
    
    return parents
    


if __name__ == '__main__':
    
    fits = []
    fig = plt.figure(figsize=(10,5))

    ax1 = fig.add_subplot(111)

    temp_indi_fit = []
    temp_pop = None

    min_temp_score = 0
    
    for i in range(1000):
        population = create_population(pop_size)
        
        population = sorted(population, key = lambda x:fitness(x), reverse = False)

        temp_indi_fit.append(fitness(population[0]))
        temp_pop = crossover(population)

        min_temp_score = min(temp_indi_fit)
        
        if (fitness(temp_pop[0]) > min_temp_score):
            fits.append(min_temp_score)
            print(min_temp_score)
            continue
        
        

    print(len(fits))
    ax1.plot(fits)

    plt.show()























