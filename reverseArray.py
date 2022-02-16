def reverseArray(A):
  return A[::-1]

def reverseString(s):
  p = 0
  r = len(s)-1
  while(p < r):
    tmp = s[p]
    s[p] = s[r]
    s[r] = tmp
    p += 1
    r -= 1

A = [1,2,3,4]
print(reverseArray(A))