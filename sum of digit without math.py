def getdata():
  a=input("enter the number")
  return a
def sums():
  a=getdata()
  a=list(a)
  sum=0
  for i in a:
    sum = sum + int(i)
  return sum
print(sums())