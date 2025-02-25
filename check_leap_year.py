def getdata():
  a=int(input("Enter a year : "))
  return a
def checkleap():
  a=getdata()
  if a%4==0 or ( a%400==0 and a%100==0):
    return "Year is Leap ."
  return "Not leap"
print(checkleap())