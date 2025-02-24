import math
def getdata():
  a=int(input("Enter a number :"))
  return a
def checkno():
  a=getdata()
  if a<=1:
    return "plz ! enter number > 1"
  else:
    for i in range(2,int(math.sqrt(a))+1):
      if a%i==0:
        return "Not prime"
  return "Yes , Number is prime ."
print(checkno())
      