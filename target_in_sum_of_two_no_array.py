def getdata():
  a=[]
  size=int(input("Enter the size of data : "))
  for i in range(size):
    a.append(int(input("Enter number : ")))
  b=int(input("Enter the target : "))
  return a,b
def checksum():
  a,b=getdata()
  c=[]
  for i in range(len(a)):
    for j in range(i):
      if a[i] + a[j] == b:
        c.append([i,j])
        continue
  if len(c)!=0:
    return ("Target is fount at index : ",c)
  else:
    return ("Target not found !!!",c)
print(checksum())