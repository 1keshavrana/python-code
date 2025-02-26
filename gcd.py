def getdata():
  a=int(input("enter the 1st number :"))
  b=int(input("enter the 2nd number :"))
  return a,b
def gcd():
  a,b=getdata()
  x=min(a,b)
  while x:
    if (a % x == 0) and (b % x == 0):
      break
    x-=1 
  return x
print(gcd())  