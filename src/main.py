# Source code program untuk mencari sepasang titik terdekat di ruang 3D 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random 
from math import * 
import time

global countDnC
# fungsi untuk meminta input 
def generateRandomDots(n):
    result = []
    for i in range(n):
        x = random.randint(0,100)
        y = random.randint(0,100)
        z = random.randint(0,100)

        titik = [x,y,z]
        result.append(titik)
    
    return result # return list of titik 

# procedure untuk print seluruh titik 
def printDots(dots):
    for i in range(len(dots)):
        print(dots[i])

# procedure untuk visualisasi seluruh titik dan 2 titik dengan jarak terdekat (SPEK BONUS)
def visualize(randomDots,closestPairIndex):
    colors = np.array(['r'] * len(randomDots))
    first = closestPairIndex[0];
    second = closestPairIndex[1];
    colors[first] = colors[second] = 'b'; 

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_dots = []
    y_dots = []
    z_dots = []

    for i in range(len(randomDots)):
        x_dots.append(randomDots[i][0])

    for i in range(len(randomDots)):
        y_dots.append(randomDots[i][1])
    
    for i in range(len(randomDots)):
        z_dots.append(randomDots[i][2])
    
    ax.scatter(x_dots, y_dots, z_dots, c = colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# fungsi untuk mendapat jarak antara titik1 dan titik2 
def getDistanceBetween(t1,t2):
    return sqrt(pow((t1[0]-t2[0]),2) + pow((t1[1]-t2[1]),2) + pow((t1[2]-t2[2]),2))

# fungsi quick sort untuk mengurutkan titik 3D terurut menaik berdasarkaan koordinat x
def quick_sort(points):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0][0] # choose x value of first point as pivot
        left = [p for p in points[1:] if p[0] <= pivot]
        right = [p for p in points[1:] if p[0] > pivot]
        return quick_sort(left) + [points[0]] + quick_sort(right)

# fungsi algoritma brute force untuk mencari closest pair
def bruteForceClosestPair(listRandomDots):
    closestPair = ()
    closestPairIndex = ()
    size = len(listRandomDots)
    minDistance = None
    countStep = 0
    initTime = time.time() * 1000
    for i in range(size):
        for j in range(i+1,size):
            t1 = listRandomDots[i]
            t2 = listRandomDots[j]
            distance = getDistanceBetween(t1,t2)
            if minDistance == None:
                minDistance = distance
                closestPair = (t1,t2)
                closestPairIndex = (i,j)
            elif distance < minDistance:
                minDistance = distance
                closestPair = (t1,t2)
                closestPairIndex = (i,j)
            countStep += 1
    
    doneTime = time.time() * 1000
    exeTime = doneTime - initTime
    
    return (closestPair, minDistance, exeTime, countStep, closestPairIndex)

# impementasi algoritma DnC untuk menyelesaikan masalah closest pair 
def DnCClosestPair(listRandomDots):
    pass 



def closest_pair(points):
    countDnc = 0
    n = len(points)
    if n <= 3:
        return brute_force_closest_pair(points)
    mid = n // 2
    left_points = points[:mid]
    right_points = points[mid:]
    left_closest = closest_pair(left_points)
    right_closest = closest_pair(right_points)
    closest = min(left_closest, right_closest)
    mid_points = []
    for point in points:
        if abs(point[0] - points[mid][0]) < closest:
            mid_points.append(point)
            # countDnc += 1
    mid_points.sort(key=lambda x: x[1])
    mid_closest = closest
    for i in range(len(mid_points)):
        for j in range(i + 1, len(mid_points)):
            if mid_points[j][1] - mid_points[i][1] >= mid_closest:
                break
            dist = distance(mid_points[i], mid_points[j])
            countDnc += 1
            if dist < mid_closest:
                mid_closest = dist
    return min(closest, mid_closest)


def brute_force_closest_pair(points):
    n = len(points)
    closest = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < closest:
                closest = dist
    return closest


def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# fungsi untuk menampilkan output hasil run 
def printOutput(hasil):
    print("Hasil dari run ini adalah sebagai berikut : ")
    print()
    print("Pasangan titik terdekat: ", hasil[0])
    print("Jarak pasangan titik terdekat: ", hasil[1])
    print(f'Waktu eksekusi: {hasil[2]} milisekon')
    print("Jumlah perhitungan rumus Euclidian: ", hasil[3])

    print()
    print("##################################################")
    print()
    answer = input("[y/n]: ").lower()
    if answer == 'y':
        visualize(randomDots,hasil[4])
        
    
    print("Terima kasih telah menggunakan program ini ^-^")
    print()
    
    
# main program 
if __name__ == '__main__' :
    
    print("SELEMAT DATANG DI PROGRAM MENCARI PASANGAN TITIK TERDEKAT")
    print()
    n = int(input("Masukkan jumlah titik (n): "))
    randomDots = generateRandomDots(n)
    hasil = bruteForceClosestPair(randomDots)

    printOutput(hasil)




    # successCase = 0 
    # n = int(input("Masukkan jumlah percobaan : "))
    # k = int(input("Masukkan jumlah titik untuk tiap percobaan : "))
    # startTime = time.time() * 1000
    # for i in range(n):
    #     randomDots = generateRandomDots(k)
    #     hasil = bruteForceClosestPair(randomDots)
    #     hasil2 = closest_pair((quick_sort(randomDots)))
        
    #     if hasil[1] == hasil2:
    #         successCase += 1
    # endTime = time.time() * 1000

    # computationTime = endTime - startTime
    # print("Waktu Eksekusi =", computationTime)
    
    # print((successCase / n) * 100)


