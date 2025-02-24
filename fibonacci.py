def getdata():
  a=int(input("Enter the size of fibonacci : "))
  return a
def fibo():
  a=getdata()
  f1=0
  f2=1
  fb=0
  print(f1,f2,end=' ')
  for i in range(1,a-1):
    fb=f2+f1
    f1=f2
    f2=fb
    print(fb,end=' ')
  return
fibo()