def getdata():
  a=int(input("enter the 1st number :"))
  b=int(input("enter the 2nd number :"))
  return a,b
def lcm():
  a,b=getdata()
  gr=max(a,b)
  sm=min(a,b)
  for i in range(gr,a*b+1,gr):
    if i % sm == 0:
      return i
print(lcm())  