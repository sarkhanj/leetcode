def binarySearch(A, key):
  start = 0
  end = len(A)
  mid = (start + end) // 2
  while(start < end):
    if A[mid] > key:
      end = mid
    elif A[mid] < key:
      start = mid+1
    else:
      return mid
    mid = (start + end) // 2


A = [1,2,3,4,5,6,7,8]
print(binarySearch(A,1))

print 2d array diagonally