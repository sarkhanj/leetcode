A = [1,2,33,5,6,4,22,11]
for j in range(1, len(A)):
    key = A[j] 
    i = j - 1 
    while(i >= 0 and A[i] > key):
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)

def binarySearchIterative(A, key):
    p = 0
    r = len(A)
    q = (p+r) // 2
    while q > 1:
        if A[q] > key:
            r = q
        elif A[q] < key:
            p = q+1
        else:
            return q
        q = (p+r) // 2