A = [1,2,3,4,5,6,7,8]

def binarySearchIterative(A, key):
    p = 0
    r = len(A)
    q = (p+r) // 2
    while p < r:
        if A[q] > key:
            r = q
        elif A[q] < key:
            p = q+1
        else:
            return q
        q = (p+r) // 2


def binarySearchRecursive(A, key, low, high):
    if low > high:
        return None
    mid = (low+high) // 2
    if A[mid] == key:
        return mid
    if key > mid:
        return binarySearchRecursive(A, key, mid+1,high)
    else:
        return binarySearchRecursive(A, key, low, mid-1)

print(binarySearchIterative(A, 1))
print(binarySearchRecursive(A,1,0,len(A)))