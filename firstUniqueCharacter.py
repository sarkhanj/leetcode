def firstUniqChar( s):
  dict = []
  for i in range(len(s)):
    if s[i] in dict:
      dict.remove(s[i])
    else:
      dict.append(s[i])
      
  if dict:
    return dict[0]
  return -1


print(firstUniqChar("loveleetcode"))
