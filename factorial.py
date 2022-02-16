num = 4;

def factorial(num):
  if num == 0:
    return 1
  else:
    fact = 1;
    for i in range(1,num+1):
      fact *= i;
    return fact;


def factorialRecursive(num):
  return 1 if (num == 0 or num == 1) else num*factorialRecursive(num-1)

print(factorialRecursive(num))
