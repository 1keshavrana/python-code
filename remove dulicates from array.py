def getdata():
  a=[]
  size_a=int(input("enter the size of array 1 : "))
  for i in range (size_a):
    a.append(int(input()))
  return a
def dulicate():
  a=getdata()
  return set(a)
print(dulicate())