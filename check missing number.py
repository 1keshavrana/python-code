def getdata():
  arr=[]
  size=int(input("enter size of array : "))
  for i in range(size):
    arr.append(int(input()))
  return arr
def searchelement():
  arr=getdata()
  searchfor=int(input("enter the element for searching : "))
  print("element is found in array ") if searchfor in arr else print("not found")
searchelement()