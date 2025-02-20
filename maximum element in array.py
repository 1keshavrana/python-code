def getdata():
    arr=int(input("number of element in array : "))
    array1=[]
    for i in range(0,arr):
      array1.append(int(input()))
    return array1
def mxelement():
  max1=max(getdata())
  return max1
a=mxelement()
print("Maximum element in array is ",a)