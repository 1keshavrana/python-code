def getdata():
  a=[]
  size=int(input("enter the size of array : "))
  for i in range(size):
    a.append(int(input()))
  return a
def secndlrgele():
  a=getdata()
  a.sort()
  return a[len(a)-2]
print("The second largest element in array is : ", secndlrgele())
  