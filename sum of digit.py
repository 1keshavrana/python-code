def getdata():
  a=int(input("Enter the number to find sum of their digits : "))
  return a
def sumdigit():
  a=getdata()
  sum=0
  while a>0:
    r=a%10
    a=int(a/10)
    sum=sum+r
  return sum
print("Sum if digits is : ",sumdigit())