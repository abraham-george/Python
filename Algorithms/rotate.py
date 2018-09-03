'''
This is a program to rotate a nxn array by 90 degrees clockwise.
'''

def rotate(arr):
    size = len(arr) - 1
    for i in range(len(arr) // 2):
        for j in range(i, size - i):
            (arr[i][j], arr[-(j+1)][i], arr[-(i+1)][-(j+1)], arr[j][-(i+1)]) = (arr[-(j+1)][i], arr[-(i+1)][-(j+1)], arr[j][-(i+1)], arr[i][j])

    for i in range(len(arr)):
        print(arr[i])

rotate([[1,2,3], [4,5,6], [7,8,9]])
