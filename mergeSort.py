import math

def mergeSort(A):
    if len(A) > 1:
        L = A[:len(A)//2]
        R = A[len(A)//2:]

        # recursion
        mergeSort(L)
        mergeSort(R)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
            
A = [2,6,5,1,7,4,3]
mergeSort(A)
print(A)      