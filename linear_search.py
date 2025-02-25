def getdata():
  a=[]
  size=int(input("Enter the size of data : "))
  for i in range(size):
    a.append(int(input("Enter number : ")))
  return a
def linearsrch():
  a=getdata()
  elemnt=int(input("enter the element search for : "))
  for i in a:
    if elemnt==i:
      return ("element is found")
  return "element not found"
print(linearsrch())