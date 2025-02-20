def getdata():
  st=input()
  return st
def palindrome():
  st=getdata()
  rst=st[::-1]
  if st==rst:
    print("Entered string is palindrome ...")
  else:
    print("Not palindrome")
  
palindrome()