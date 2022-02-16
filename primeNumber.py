# write prime numbers until the given number. 10 = 2,3,5,7

# lower = int(input("Enter starting val: "));
# higher = int(input("Enter ending val: "));
lower = 10
higher = 20
for i in range(lower,higher):
  for j in range(2,i):
    if(i % j == 0):
      break
  else:
    print(i)
