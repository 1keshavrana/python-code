def getdata():
  a=int(input("Enter the number to check for Armstrong : "))
  return a
def checkarmstrong():
  sum=0
  a=getdata()
  b=a
  while a>0:
    r=a%10
    sum=sum+(r*r*r)
    a=a//10
  if sum==b:
    return "Number is Armstrong ."
  return "Not armstrong !"
print(checkarmstrong())