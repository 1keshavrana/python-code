def getdata():
  a=int(input("Enter the base : "))
  b=int(input("Enter the power : "))
  return a,b
def power():
  a,b=getdata()
  result=1
  if b==0:
    return result
  for i in range(b):
    result*=a
  return ("Power of entered base is : ",result)
print(power())