def getdata():
  a=[]
  size=int(input("Enter the size of data : "))
  for i in range(size):
    a.append(int(input("Enter number : ")))
  return a
def selectionsort():
  a=getdata()
  for i in range(0,len(a)):
    for j in range(0,i):
      if a[j]>a[i]:
        t=a[i]
        a[i]=a[j]
        a[j]=t
  return a
print(selectionsort())