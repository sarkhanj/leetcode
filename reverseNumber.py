def reverse_slicing(s):
  s = str(s)
  return s[::-1]

def reverseWithNums(My_Number):
  Reverse_Number = 0
  while(My_Number > 0):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
    My_Number = My_Number //10
  print("Reverse of the provided number is = %d" %Reverse_Number)


def reverse(x):
    if x < 0:
            x = str(abs(x))
            x = int("-"+x[::-1])
            if x < pow(-2, 31) or x > (pow(2, 31) - 1):
                return 0
            return x
        x = str(x)
        x = int(x[::-1])
        if x < pow(-2, 31) or x > (pow(2, 31) - 1):
            return 0
        return x


if 1534236469 > pow(2, 31) - 1:
  print("bigger")
# print('Reversing the given number using slicing =' + reverse_slicing(1234567))
# reverseWithNums(1234)
print(reverse(1534236469))
