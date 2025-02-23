def getdata():
  a=int(input("Enter the number to find factorial : "))
  return a
def fact():
  a=getdata()
  fact=1
  for i in range(1,a+1):
    fact = fact * i
  return fact
print(fact())