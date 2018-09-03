'''
This is a program to multiply 2 arrays.
'''
def matrix_multiplication(A,B,n):
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])
    return C

print(matrix_multiplication([[1,2],[3,4]], [[5,6], [7,8]], 2))

# The time complexity for this algorithm is of the order -> O(n^3)