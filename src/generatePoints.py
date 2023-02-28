# file : generatePoints.py 
# berfungsi untuk menghasilkan titik 3 dimensi dan juga n-dimensi secara random sesuai dengan masukan jumlah titik
# domain dari titik adalah -100 sampai dengan 100 
# setiap koordinat sumbu spesifik hingga 3 desimal

import random 

# fungsi untuk menggenerate titik sejumlah n dalam ruang 3D 
def generateRandom3DPoints(n):
    points = []
    for i in range(n):
        x = round(random.uniform(-100,100),3)
        y= round(random.uniform(-100,100),3)
        z = round(random.uniform(-100,100),3)

        point = [x,y,z]
        points.append(point)
    
    return points # return list of titik 


# fungsi untuk menggenerate titik sejumlah n dalam ruang k-D
def generatePoint(n,k):
    points = []
    for i in range(n):
        point = []
        for i in range(k):
            t = round(random.uniform(-100,100),3)
            point.append(t)
        points.append(point)
    
    return points 