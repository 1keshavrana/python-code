def getdata():
  a=[]
  size_a=int(input("enter the size of array 1 : "))
  for i in range (size_a):
    a.append(int(input()))
  return a
def countele():
  a=getdata()
  b=set(a)
  cout=0
  for i in b:
    for j in a:
      if i==j:
        cout+=1
    print("element ",i,"occurrence is : ",cout)
    cout=0
countele()