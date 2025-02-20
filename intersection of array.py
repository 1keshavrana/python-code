def getdata():
  a=[]
  size_a=int(input("enter the size of array 1 :"))
  print("enter the elements of array 1")
  for i in range(size_a):
    a.append(int(input()))
  return a
def getdata1():
  b=[]
  size_b=int(input("enter the size of array 2 :"))
  print("enter the elements of array 1")
  for j in range(size_b):
    b.append(int(input()))
  return b
def intersection():
  a=getdata()
  b=getdata1()
  c=[]
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i]==b[j]:
        c.append(a[i])
  return set(c)3
intersection()
