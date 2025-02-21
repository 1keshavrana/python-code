def getdata():
  a=[]
  size_a=int(input("enter the size of array A : "))
  for i in range(size_a):
    a.append(int(input()))
  return a
def getdata1():
  b=[]
  size_b=int(input("enter the size of array B : "))
  for i in range(size_b):
    b.append(int(input()))
  return b
def mergearray():
  a=getdata()
  b=getdata1()
  a.extend(b)
  a.sort()
  return a
print(mergearray())