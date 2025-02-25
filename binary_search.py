def getdata():
  a=[]
  size=int(input("enter the size of data : "))
  for i in range(size):
    a.append(int(input("Enter the number : ")))
  return a
def binarysrch():
  a=getdata()
  a.sort()
  elemnt=int(input("Enter the element search for : "))
  beg=0
  last=len(a)-1
  while last>=beg:
    mid=(beg+last)//2
    if a[mid]==elemnt:
      return "element is found"
    elif a[mid]>elemnt:
      last=mid-1
    else:
      beg=mid+1
  return "element is not found"
print(binarysrch())