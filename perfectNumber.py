def perfectNumber(n):
  divisors = 0
  for i in range(1,n):
    if(n%i == 0):
      divisors += i
  if(divisors == n):
    print("Perfect Number")
    return True
  print("NOT Perfect Number")
  return False


perfectNumber(25)