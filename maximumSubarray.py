import math


def findMaxCrossingSubarray(A, low, mid, high):
    leftSum = -1
    maxRight = summ = maxLeft = 0
    for i in range(mid,low,-1):
        summ += A[i]
        if summ > leftSum:
            leftSum = summ
            maxLeft = i
    print("leftSum = " + str(leftSum))
    rightSum = -1
    summ = 0
    for j in range(mid+1, high):
        summ += A[j]
        if summ > rightSum:
            rightSum = summ
            maxRight = j
    print("rightSum = " + str(rightSum))
    return (maxLeft, maxRight, leftSum+rightSum)


def findMaximumSubarray(A, low, high):
    if high == low:
        print(low, high)
        return (low, high, A[low])
    else:
        mid = int(math.floor(low+high/2))
        (leftLow,leftHigh,leftSum) = findMaximumSubarray(A,low,mid)
        
        (rightLow,rightHigh,rightSum) = findMaximumSubarray(A,mid+1,high)
        (crossLow,crossHigh,crossSum) = findMaxCrossingSubarray(A,low,mid,high)
        if leftSum > rightSum and leftSum > crossSum:
            return (leftLow,leftHigh,leftSum)
        elif rightSum > leftSum and rightSum > crossSum:
            return (rightLow,rightHigh,rightSum)
        else:
            return (crossLow,crossHigh,crossSum)


A = [2,4,1,10,20,30,3,2,5]

# print(findMaxCrossingSubarray(A,0,int(math.floor(len(A)/2)),len(A)))
print(findMaximumSubarray(A,0,len(A)))
