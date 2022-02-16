def duplicateNums(A):
  for i in A:
    if A.count(i) == 2:
      return i
  return -1


def removeDuplicate(A):
  for i in A:
    if A.count(i) == 2:
      A.remove(i)


def removeDuplicatesWithoutLib(A):
  dict = {}
  B = []
  for i in A:
    if i in dict:
      dict[i] += 1
    else:
      dict[i]  = 0
  
  for key in dict:
    B.append(key)
  return B




A = [1,2,2,3,4]
print(duplicateNums(A))
# removeDuplicate(A)
A = removeDuplicatesWithoutLib(A)
print(A)

