def getdata():
  a=input("Enter 1st string : ")
  b=input("Enter 2nd string : ")
  return a,b
def checkanagram():
  a,b=getdata()
  a=sorted(a)
  b=sorted(b)
  if a==b:
    return "Valid Anagram ."
  else:
    return "Not Valid Anagram !!!"
print(checkanagram())