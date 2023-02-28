# file : closestPair3D.py
# Source code program untuk mencari sepasang titik terdekat di ruang 3D 
# Tersedia algoritma brute force dan juga Divide and Conquer


# import external module
from math import sqrt, pow
import time
from sort import quickSort

# fungsi untuk mendapat jarak antara titik1 dan titik2 
def getDistanceBetween3D(p1,p2):
    return sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2) + pow((p1[2]-p2[2]),2))


# fungsi algoritma brute force untuk mencari closest pair
def bruteForceClosestPair3D(listRandomDots):
    closestPair = ()
    closestPairIndex = ()
    size = len(listRandomDots)
    minDistance = None
    countStep = 0
    initTime = time.time() * 1000
    for i in range(size):
        for j in range(i+1,size):
            p1 = listRandomDots[i]
            p2 = listRandomDots[j]
            distance = getDistanceBetween3D(p1,p2)
            if minDistance is None:
                minDistance = distance
                closestPair = (p1,p2)
                closestPairIndex = (i,j)
            elif distance < minDistance:
                minDistance = distance
                closestPair = (p1,p2)
                closestPairIndex = (i,j)
            countStep += 1

    endTime = time.time() * 1000
    exeTime = endTime - initTime

    return (closestPair, minDistance, exeTime, countStep, closestPairIndex)