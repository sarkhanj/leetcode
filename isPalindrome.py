def isPalindrome(s):
  
  # print(s[::-1].lower())
  return s== s[::-1]


def isPalindromeAdvanced(s):

  getVals = list([val for val in s if val.isalnum()])
  result = "".join(getVals).lower()
  return result == result[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindromeAdvanced("A man, a plan, a canal: Panama"))
