# file : sort.py 

# fungsi quick sort untuk mengurutkan titik terurut menaik berdasarkaan koordinat sebuah sumbu n
# n = 0, maka x 
# n = 1, maka y, dst..
def quickSort(points,n):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0][n] # choose x value of first point as pivot
        left = [p for p in points[1:] if p[n] <= pivot]
        right = [p for p in points[1:] if p[n] > pivot]
        return quickSort(left,n) + [points[0]] + quickSort(right,n)