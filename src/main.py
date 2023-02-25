# Source code program untuk mencari sepasang titik terdekat di ruang 3D 

# import external module
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random 
from math import * 
import time
import pyfiglet 

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
def visualize(randomDots,closestPairCoordinate):
    print()
    print("Sepasang titik berwarna biru menunjukkan sepasang titik terdekat.")
    print()
    print("Menampilkan visualisasi data...")
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    

    # mewarnai seluruh titik dengan warna merah
    colors = np.array(['r'] * len(randomDots))
    first = closestPairCoordinate[0];
    second = closestPairCoordinate[1];
    pertama = 0
    kedua = 0

    # mencari index titik dalam kumpulan titik
    for i in range(len(randomDots)):
        case1 = (randomDots[i][0] == first[0] and randomDots[i][1] == first[1] and randomDots[i][2] == first[2])
        case2 = (randomDots[i][0] == second[0] and randomDots[i][1] == second[1] and randomDots[i][2] == second[2])
        if(case1 or case2):
            pertama = i
            break
    
    # mencari index pasangan titik lainnya dalam kumpulan titik
    for j in range(pertama+1,len(randomDots)):
        
        if(case1):
            # jika menemukan titik pertama terlebih dahulu, berarti yang selanjutnya dicari adalah titik kedua
            toSearch = (randomDots[j][0] == second[0] and randomDots[j][1] == second[1] and randomDots[j][2] == second[2])
        elif(case2):
            # menemukan titik kedua terlebih dahulu, berarti yang selanjutnya dicari adalah titik pertama
            toSearch = (randomDots[j][0] == first[0] and randomDots[j][1] == first[1] and randomDots[j][2] == first[2])
        
        if((toSearch)):
            kedua = j
            break
    
    # mengganti warna sepasang titik terdekat dengan warna biru
    colors[pertama] = colors[kedua] = 'b'

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
    
    endTime = time.time() * 1000
    exeTime = endTime - initTime
    
    return (closestPair, minDistance, exeTime, countStep, closestPairIndex)


# fungsi Divide and Conquer untuk mencari sepasang titik terdekat
def closest_pair(listRandomDots):
    global countSteps

    # kasus basis, bisa selesaikan dengan bruteForce karena n bernilai cukup kecil
    n = len(listRandomDots)
    if n <= 3:
        m = bruteForceClosestPair(listRandomDots)
        countSteps += m[3]
        return (m[1],m[0])
    
    # cari titik tengah untuk membagi kumpulan titik menjadi dua bagian
    # dengan jumlah yang sama banyak 
    mid = n // 2

    # bagi titik menjadi 2 himpunan, yaitu kiri dan kanan
    left_points = listRandomDots[:mid]
    right_points = listRandomDots[mid:]

    # cari closest pair pada kedua bagian himpunan secara rekursif 
    left_closest = closest_pair(left_points)
    right_closest = closest_pair(right_points)

    # ambil pasangan titik dengan jarak terdekat di antara kiri atau kanan
    if min(left_closest[0], right_closest[0]) == left_closest[0]:
        closest_pairs = left_closest[1]
    else:
        closest_pairs = right_closest[1]
    
    closest = min(left_closest[0], right_closest[0])

    # lakukan pengecekan lagi untuk titik-titik di sekitar garis bagi
    mid_points = []
    for dots in listRandomDots:
        if abs(dots[0] - listRandomDots[mid][0]) < closest:
            mid_points.append(dots)

    mid_points.sort(key=lambda x: x[1])
    mid_closest = closest
    for i in range(len(mid_points)):
        for j in range(i + 1, len(mid_points)):
            if mid_points[j][1] - mid_points[i][1] >= mid_closest:
                break
            dist = getDistanceBetween(mid_points[i], mid_points[j])
            countSteps += 1 
            if dist < mid_closest:
                mid_closest = dist
                mid_closest_point = (mid_points[i],mid_points[j])

    if(min(closest,mid_closest) == closest):
        return (closest, closest_pairs)
    else:
        return (mid_closest, mid_closest_point)


def printHasil(randomDots,hasil,exeTime,countStep):
    print("Hasil dari run ini adalah sebagai berikut : ")
    print()
    print(f"Pasangan titik terdekat             : {hasil[1][0]} , {hasil[1][1]}")
    print(f"Jarak pasangan titik terdekat       : {hasil[0]} satuan")
    print(f"Waktu eksekusi program              : {exeTime} milisekon")
    print(f"Jumlah perhitungan rumus Euclidean  : {countStep}")

    print()
    print('#' * 80)
    print()
    answer = input("Ingin menampilkan visualisasi titik di ruang 3D? [y/n]: ").lower()
    if answer == 'y':
        visualize(quick_sort(randomDots),hasil[1])


def printWelcomeScreen(): 
    welcomeText = pyfiglet.figlet_format("Closest Pair 3D Solver")
    print(welcomeText)
    print()
    print('#' * 80)
    print()


def printExitScreen():
    print()
    print("#" * 80)
    print()
    exitText = pyfiglet.figlet_format("THANK YOU! ^-^")
    print(exitText)
    print()

def getAndValidateInput():
    correctInput = False
    while not correctInput:
        try:
            n = int(input("Masukkan jumlah titik (n): "))
        except:
            print("Masukkan Anda tidak sesuai, silahkan ulangi masukan Anda")
            print()
            n = "salah"
        
        if(type(n) == int):
            if(n < 1):
                print("Untuk mencari pasangan titik terdekat diperlukan minimal 2 titik!")
                print("Silakan ulangi kembali masukan.")
                print()
            else:
                correctInput = True
    
    return n


def continueOrNot():
    print()
    print('#' * 80)
    print()
    answer = False
    ask = input("Ingin mencoba jumlah titik lainnya? [y/n]: ").lower()
    if(ask == 'y'):
        answer = True
        print()
        print("#" * 80)
        print()
    
    return answer


# main program 
if __name__ == '__main__' :

    run = True
    printWelcomeScreen()

    while run:

        countSteps = 0

        n = getAndValidateInput()
        randomDots = generateRandomDots(n)
        startTime = time.time() * 1000
        hasil = closest_pair(quick_sort(randomDots))
        endTime = time.time() * 1000
        exeTime = endTime - startTime

        printHasil(randomDots,hasil,exeTime,countSteps)

        run = continueOrNot()

    printExitScreen()
    


