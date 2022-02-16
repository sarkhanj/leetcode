A = [5,4,12,6,1,3,2,20,15]

min_val = A[0]
ch = 0
changed = False

for j in range(len(A)):
    for i in range(j,len(A)):
        print(j)
        if A[i] < min_val:
            min_val = A[i]
            ch = i
            changed = True
            print(j,A[i],ch)
            
    if(j+1 <= len(A) and changed):
        temp = A[j]
        A[j] = min_val
        A[ch] = temp
        min_val = A[j+1]
        changed = False
# ???

print(A)

