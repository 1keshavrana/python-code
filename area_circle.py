def getdata():
  a=int(input("Enter the radius of circle : "))
  return a
def areacircle():
  a=getdata()
  area=(22/7)*a*a
  return ("Area of circle is : ",area)
print(areacircle())