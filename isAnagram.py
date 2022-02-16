import collections


def areAnagrams(s1,s2):
  if(len(s1) != len(s2)):
    print("NOT anagrams")
    return 0  
  dict1 = {}
  dict2 = {}
  for l in s1:
    if l in dict1:
      dict1[l] += 1
    else:
      dict1[l]  = 0
  
  for l in s2:
    if l in dict2:
      dict2[l] += 1
    else:
      dict2[l]  = 0
  if(dict1 == dict2):
    print("Strings are anagrams")
  else:
    print("Strings are NOT anagrams")

def areAnagrams2(s,t):
  counter1 = collections.Counter(s)
  counter2 = collections.Counter(t)
  print(counter1 == counter2)


areAnagrams2("hello", "olleh")
# areAnagrams("hello", "olleh")