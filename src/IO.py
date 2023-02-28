# file IO.py
# berfungsi untuk menghandle input dan output program 

# import external module 
import pyfiglet 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time 
from sort import quickSort

# prosedur untuk menampilkan menu 
def printMenu():
    print("""
   ############ MENU ###########
    1. Closest Pair 3 Dimension
    2. Closest Pair N Dimension
    3. Exit
    """)

# prosedur untuk menampilkan welcome text
def printWelcomeScreen(): 
    welcomeText = pyfiglet.figlet_format("Closest Pair 3D Solver")
    print(welcomeText)
    print()
    print('#' * 80)
    print()


# prosedur untuk menampilkan exit text
def printExitScreen():
    print()
    print("#" * 80)
    print()
    exitText = pyfiglet.figlet_format("THANK YOU! ^-^")
    print(exitText)
    print()


# fungsi untuk meminta dan memvalidasi nilai dimensi
def getAndValidateInputD():
    correctInput = False 
    while not correctInput:
        try: 
            d = int(input("Masukkan dimensi: "))
            print()
        except:
            print("Masukkan Anda tidak sesuai, silakan ulangi masukan Anda")
            print()

        if(type(d) == int):
            if(d <= 0):
                print("Dimensi tidak bisa bernilai 0 ataupun kurang dari 0")
                print("Silakan ulangi kembali masukan.")
                print()
            else:
                correctInput = True
    
    return d


# prosedur untuk minta dan validasi input n
def getAndValidateInputN():
    correctInput = False
    while not correctInput:
        try:
            n = int(input("Masukkan jumlah titik (n): "))
            print()
        except:
            print("Masukkan Anda tidak sesuai, silahkan ulangi masukan Anda")
            print()
            n = "salah"
        
        if(type(n) == int):
            if(n < 2):
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

# prosedur untuk mengeluarkan output hasil program dari algoritma divide and conquer
def printHasilDnC(randomPoints,hasil,exeTime,countStep):
    print("Hasil dari run dengan algoritma DIVIDE AND CONQUER : ")
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
        visualize3D(quickSort(randomPoints,0),hasil[1])

# prosedur untuk mengeluarkan output hasil program dari algoritma divide and conquer
def printHasilDnCND(hasil,exeTime,countStep):
    print("Hasil dari run dengan algoritma DIVIDE AND CONQUER : ")
    print()
    print(f"Pasangan titik terdekat             : {hasil[1][0]} , {hasil[1][1]}")
    print(f"Jarak pasangan titik terdekat       : {hasil[0]} satuan")
    print(f"Waktu eksekusi program              : {exeTime} milisekon")
    print(f"Jumlah perhitungan rumus Euclidean  : {countStep}")

    print()
    print('#' * 80)
    print()


# prosedur untuk mengeluarkan output hasil program dari algoritma brute force
def printHasilBruteForce(hasil):
    print("#" * 80)
    print()
    print("Hasil dari run dengan algoritma BRUTE FORCE : ")
    print()
    print(f"Pasangan titik terdekat             : {hasil[0][0]} , {hasil[0][1]}") 
    print(f"Jarak pasangan titik terdekat       : {hasil[1]} satuan")
    print(f"Waktu eksekusi                      : {hasil[2]} milisekon")
    print(f"Jumlah perhitungan rumus Euclidian  : {hasil[3]}")
    print()
    print('#' * 80)
    print()

# procedure untuk visualisasi seluruh titik dan 2 titik dengan jarak terdekat (SPEK BONUS)
def visualize3D(randomPoints,closestPairCoordinate):
    print()
    print("Sepasang titik berwarna biru menunjukkan sepasang titik terdekat.")
    print()
    print("Menampilkan visualisasi data...")
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    
    # mewarnai seluruh titik dengan warna merah
    colors = np.array(['r'] * len(randomPoints))
    first = closestPairCoordinate[0];
    second = closestPairCoordinate[1];
    pertama = 0
    kedua = 0

    # mencari index titik dalam kumpulan titik
    for i in range(len(randomPoints)):
        case1 = (randomPoints[i][0] == first[0] and randomPoints[i][1] == first[1] and randomPoints[i][2] == first[2])
        case2 = (randomPoints[i][0] == second[0] and randomPoints[i][1] == second[1] and randomPoints[i][2] == second[2])
        if(case1 or case2):
            pertama = i
            break
    
    # mencari index pasangan titik lainnya dalam kumpulan titik
    for j in range(pertama+1,len(randomPoints)):
        
        if(case1):
            # jika menemukan titik pertama terlebih dahulu, berarti yang selanjutnya dicari adalah titik kedua
            toSearch = (randomPoints[j][0] == second[0] and randomPoints[j][1] == second[1] and randomPoints[j][2] == second[2])
        elif(case2):
            # menemukan titik kedua terlebih dahulu, berarti yang selanjutnya dicari adalah titik pertama
            toSearch = (randomPoints[j][0] == first[0] and randomPoints[j][1] == first[1] and randomPoints[j][2] == first[2])
        
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

    for i in range(len(randomPoints)):
        x_dots.append(randomPoints[i][0])

    for i in range(len(randomPoints)):
        y_dots.append(randomPoints[i][1])
    
    for i in range(len(randomPoints)):
        z_dots.append(randomPoints[i][2])
    
    ax.scatter(x_dots, y_dots, z_dots, c = colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# procedure untuk print seluruh titik 
def printPoints(points):
    for i in range(len(points)):
        print(points[i])