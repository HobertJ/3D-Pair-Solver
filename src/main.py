# file : main.py 
# berisi program utama 

# import module 
from generatePoints import *
from IO import *
from closestPair3D import *
from closestPairND import *
from generatePoints import *

# fungsi Divide and Conquer untuk mencari sepasang titik terdekat di 3D
def DnCclosestPair3D(listRandomDots):
    global countSteps

    # pengurutan titik berdasarkan koordinat x nya
    listRandomDots = quickSort(listRandomDots,0)
    # kasus basis, bisa selesaikan dengan bruteForce karena n bernilai cukup kecil
    n = len(listRandomDots)
    if n <= 3:
        m = bruteForceClosestPair3D(listRandomDots)
        countSteps += m[3]
        return (m[1],m[0])
    
    # cari titik tengah untuk membagi kumpulan titik menjadi dua bagian
    # dengan jumlah yang sama banyak 
    mid = n // 2

    # bagi titik menjadi 2 himpunan, yaitu kiri dan kanan realtif terhadap titik tengah
    leftPoints = listRandomDots[:mid]
    rightPoints = listRandomDots[mid:]

    # cari closest pair pada kedua bagian himpunan secara rekursif 
    leftClosest = DnCclosestPair3D(leftPoints)
    rightClosest = DnCclosestPair3D(rightPoints)

    # ambil pasangan titik dengan jarak terdekat di antara kiri atau kanan
    if min(leftClosest[0], rightClosest[0]) == leftClosest[0]:
        closestPair = leftClosest[1]
    else:
        closestPair = rightClosest[1]
    
    closest = min(leftClosest[0], rightClosest[0])

    # lakukan pengecekan lagi untuk titik-titik di sekitar garis bagi
    midPoints = []
    for dots in listRandomDots:
        if abs(dots[0] - listRandomDots[mid][0]) < closest:
            midPoints.append(dots)

    # pengurutan titik midpoint berdasarkan nilai sumbu y nya
    midPoints = quickSort(midPoints,1)
    midClosest = closest
    for i in range(len(midPoints)):
        for j in range(i + 1, len(midPoints)):
            if midPoints[j][1] - midPoints[i][1] >= midClosest:
                break
            dist = getDistanceBetween3D(midPoints[i], midPoints[j])
            countSteps += 1 
            if dist < midClosest:
                midClosest = dist
                midClosestPair = (midPoints[i],midPoints[j])

    if(min(closest,midClosest) == closest):
        return (closest, closestPair)
    else:
        return (midClosest, midClosestPair)


# fungsi Divide and Conquer untuk mencari sepasang titik terdekat di N-D
def DnCclosestPairND(points):
    global countStepN

    if len(points) <= 3:
        m = bruteForceClosestPairND(points)
        countStepN += m[3]
        return (m[1], m[0])
    
    points = quickSort(points,0)
    
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    
    leftClosest = DnCclosestPairND(left)
    rightClosest = DnCclosestPairND(right)

    d = min(leftClosest[0], rightClosest[0])

    if(d == leftClosest[0]):
        closestPair = leftClosest[1]
    else:
        closestPair = rightClosest[1]
    
    mid_x = points[mid][0]
    strip = [p for p in points if abs(p[0] - mid_x) < d]
    
    strip = quickSort(strip,1)  
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= d:
                break
            dist = getDistanceBetweenND(strip[i], strip[j])
            countStepN += 1
            if dist < d:
                d = dist
                closestPair = (strip[i],strip[j])
        
    return (d, closestPair)


def main():
    global countStepN
    global countSteps

    run = True 
    printWelcomeScreen()

    while (run):
        countSteps = 0
        countStepN = 0
        printMenu()
        inputValid = False

        while(not inputValid):
            try:
                choice = int(input("Masukkan pilihan anda (1-3): "))
                if(1 <= choice <= 3):
                    inputValid = True
                    print()
                    if(choice == 1):
                        print("Penyelesaian masalah closest pair pada 3 Dimensi")
                        print()
                    elif(choice == 2):
                        print("Penyelesaian masalah closest pair pada N Dimensi")
                        print()
                    
                else: 
                    print()
                    print("Input tidak valid!, silakan ulangi masukan Anda!")
                    print()
            except: 
                print("Masukan Anda salah!")
                print("Silahkan ulangi kembali masukan.")
                print()
        
        if(choice == 1):
            # ambil input n 
            n = getAndValidateInputN()

            # generate titik random 
            randomPoints = generateRandom3DPoints(n)

            # eksekusi algoritma DNC
            startTime = time.time() * 1000
            hasil_dnc = DnCclosestPair3D(randomPoints)
            endTime = time.time() * 1000
            exeTime = endTime - startTime

            hasil_BF = bruteForceClosestPair3D(randomPoints)

            printHasilBruteForce(hasil_BF)
            printHasilDnC(randomPoints,hasil_dnc,exeTime,countSteps)
        
        elif(choice == 2):
            # ambil input n
            n = getAndValidateInputN()
            d = getAndValidateInputD()

            # generate titik random
            randomPoints = generatePoint(n,d)


            hasil_BF = bruteForceClosestPairND(randomPoints)

            if(d == 3):
                startTime = time.time() * 1000
                hasil_dnc = DnCclosestPair3D(randomPoints)
                endTime = time.time() * 1000
                exeTime = endTime - startTime
                printHasilBruteForce(hasil_BF)
                printHasilDnC(hasil_dnc,exeTime,countSteps)
            else:
                startTime = time.time() * 1000
                hasil_dnc = DnCclosestPairND(randomPoints)
                endTime = time.time() * 1000
                exeTime = endTime - startTime
                printHasilBruteForce(hasil_BF)
                printHasilDnCND(hasil_dnc,exeTime,countStepN)
        
        else:
            run = False
    
    printExitScreen()
        
        
# main program 
if __name__ == '__main__' :
    main()
