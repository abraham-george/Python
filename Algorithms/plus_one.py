'''
Write a program which takes as input an array of digits representing an integer D, updates the array to represent the integer D+1
'''

def plus_one(A):
    A[-1] += 1
    A = A[::-1]
    for i in range(len(A)):
        carry = 0
        if (A[i] == 10):
            A[i] = 0
            carry = 1
        if(i+1 < len(A) and carry == 1):
            A[i+1] += carry
            carry = 0
    if(carry == 1):
        A.append(carry)
    return A[::-1]

print(plus_one([9,9,9]))

# Time complexity of this algorithm is O(n)