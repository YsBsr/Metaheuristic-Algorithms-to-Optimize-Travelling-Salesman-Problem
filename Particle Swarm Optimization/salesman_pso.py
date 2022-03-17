import matplotlib.pyplot as plt

import random

from Coordinate import Coordinate

import tsplib95

import numpy 

import os

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

problem = tsplib95.load(os.getcwd() + '\\berlin52.tsp')
#berlin52.tsp dosyasını tsplib95 kütüphanesi ile okuyoruz.

nodes = problem.node_coords.values()
#tsplib95 kütüphanesi berlin95.tsp dosyasındaki konumları okuduktan sonra
#bu konumları bir dictionary veri yapısında tutar (key-value çiftleri ile)
#bu dictionarydeki valueler bizim 52 tane konumuzun birer birer (x, y) koordinatlarıdır.

indis = 0

for x, y in problem.node_coords.values():
    coordinates.append(Coordinate(x, y, indis))
    indis += 1

    #En yukarda import ettiğim Coordinate class'ını kullanarak
    #coordinates listemi berlin52.tsp dosyasının içindeki koordinatlar(konumlar)
    #ile dolduruyorum.

length = len(coordinates)

particle_size = 20

velocity_pb = []

velocity_gb = []

def calculate_Pid_Xid(particle, alfa):

    particle_with_new_location = copy_array(particle)

    for i in range(len(velocity_pb)):
        if (alfa >= numpy.random.randint(0, 1)):
            temp = particle_with_new_location[velocity_pb[i][0]]
            particle_with_new_location[velocity_pb[i][0]] = particle_with_new_location[velocity_pb[i][1]]
            particle_with_new_location[velocity_pb[i][1]] = temp

    return particle_with_new_location


def calculate_Pig_Xid(particle, beta):

    particle_with_new_location = copy_array(particle)

    for i in range(len(velocity_gb)):
        if (beta >= numpy.random.randint(0, 1)):
            temp = particle_with_new_location[velocity_gb[i][0]]
            particle_with_new_location[velocity_gb[i][0]] = particle_with_new_location[velocity_gb[i][1]]
            particle_with_new_location[velocity_gb[i][1]] = temp

    return particle_with_new_location

def velocity_g(particle, best_particle):

    new_array1 = copy_array(particle)
    new_array2 = copy_array(best_particle)

    for i in range(0, length):
        for j in range(0, length):
            if (new_array1[i].indis == new_array1[j].indis):
                if (i == j):
                    continue
                velocity_gb.append([new_array1[i].indis, new_array1[j].indis])

    """print(velocity_gb)
    print(len(velocity_gb))
    
    while(1):
        continue"""

def velocity_p(particle):

    minn = Coordinate.get_distance(particle[0], particle[1])

    for i in range(length):
        for j in range(length):
            
            if (particle[i].indis == particle[j].indis):
                continue
            
            if (minn >= Coordinate.get_distance(particle[i], particle[j])):
                minn = Coordinate.get_distance(particle[i], particle[j])
                swap = [particle[i].indis, particle[j].indis]

                velocity_pb.append(swap)
    
    """print(velocity_pb)
    print(len(velocity_pb))
    
    while(1):
        continue"""

def copy_array(array):

    new_array= []

    for i in array:
        new_array.append(i)

    return new_array

def create_random_solution(particle_size):

    random_solution = []

    indis = 0

    for i in range(particle_size):
        random_solution.append([coordinates[numpy.random.randint(0, length - 1)] for i in range(length)])

    return random_solution

def find_personal_best_score_info(particle):

    pb = Coordinate.get_total_distance(particle)

    return pb

def find_global_best_score_info(all_particles):

    gb = find_personal_best_score_info(all_particles[0])

    indis = 0

    for i in all_particles:
        if (gb > find_personal_best_score_info(i)):
            gb = find_personal_best_score_info(i)
            indis += 1

    return [gb, indis]
    

if __name__ == '__main__':

    particle_swarm = create_random_solution(particle_size)

    fig = plt.figure(figsize=(10,5))

    ax1 = fig.add_subplot(111)

    hh = []

    first_puan = 0
    new_puan = 0

    temp_particle = None
            
    print("Wait for the graph screen.")        
            
    for i in range(400):

        a = find_global_best_score_info(particle_swarm)

        for t in range(particle_size):
        
            if (t == a[1]):
                continue
            
            velocity_p(particle_swarm[t]),

            first_puan = find_personal_best_score_info(particle_swarm[t])

            temp_particle = calculate_Pid_Xid(particle_swarm[t], 0.5)

            new_puan = find_personal_best_score_info(temp_particle)

            if (new_puan >= first_puan):
                continue
            
            particle_swarm[t] = temp_particle

            velocity_pb.clear()

        for k in range(particle_size):

            if (k == a[1]):
                continue

            velocity_g(particle_swarm[k], particle_swarm[a[1]])
            
            particle_swarm[k] = calculate_Pig_Xid(particle_swarm[k], 0.5)

            velocity_gb.clear()

        #print(a[0])
        hh.append(a[0])
        
        
    ax1.plot(hh)

    plt.show()
    
    
