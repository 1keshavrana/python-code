def getdata():
  a=[]
  for i in range(3):
    a.append(int(input("enter number :")))
  return a
def maxno():
  a=getdata()
  if a[0]>a[1] and a[1]>a[2]:
    return ("Max is : ",a[0])
  elif a[2]>a[0]:
    return ("Max is : ",a[2])
  else:
    return ("Max is : ",a[1])
maxno()