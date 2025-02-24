def getdata():
  s=input("Enter The Paragraph :")
  return s
def countword():
  s=getdata()
  print("The total lenght of word in string is : ",len(list(s.split(' '))))
countword()