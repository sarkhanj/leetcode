def bubbleSort(A):
  for i in range(len(A)):
    for j in range(len(A)):
      if A[i] < A[j]:
        tmp = A[j]
        A[j] = A[i]
        A[i] = tmp


A = [2,4,1,5,3,3]
bubbleSort(A)
print(A)