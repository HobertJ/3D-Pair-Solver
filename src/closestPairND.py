# file : closestPairND.py
# Source code program untuk mencari sepasang titik terdekat di ruang 3D 
# Tersedia algoritma brute force dan juga Divide and Conquer

import math 
import time 
from generatePoints import generatePoint
from sort import quickSort

def getDistanceBetweenND(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(len(p1))))


def bruteForceClosestPairND(points):
    closestPair = ()
    minDistance = None
    countStep = 0
    size = len(points)
    initTime = time.time() * 1000
    for i in range(size):
        for j in range(i+1, size):
            p1 = points[i]
            p2 = points[j]
            distance = getDistanceBetweenND(p1,p2)
            if minDistance is None:
                minDistance = distance
                closestPair = (p1,p2)
            elif distance < minDistance:
                minDistance = distance
                closestPair = (p1,p2)
            countStep += 1
    endTime = time.time() * 1000
    exeTime = endTime - initTime 
            
    return (closestPair, minDistance, exeTime, countStep)