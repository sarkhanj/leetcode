def plusOne(digits):

    if(digits[-1] != 9):
        digits[-1] += 1
        return digits

    l = len(digits) - 1
    number = 0
    for i in digits:
        number += i*pow(10, l)
        l -= 1
    number += 1

    digs = []
    digit = number % 10
    while(number > 0):
        digs.insert(0, digit)
        # digs.append(digit)
        number = number//10
        digit = number % 10
    return digs


print(plusOne([9]))