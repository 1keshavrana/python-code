import math
pi=22/7
class shape:
  def __init__(self) -> None:
    pass
class Circle(shape):
  def areacircle(self):
    r=int(input("Radius of circle is : "))
    return "Area is : ",(22/7)*r*r

class rectangle(shape):
  def arearectangle(self):
    a=int(input("One side is : "))
    b=int(input("Second side is : "))
    return "Area is : ",a*b

class square(shape):
  def areasquare(self):
    a=int(input("One Side is : "))
    return "Area is : ",a*a

class triangle(shape):
  def areatriangle4(self):
    a=int(input("One Side is : "))
    b=int(input("Second side is : "))
    c=int(input("Third side is : "))
    s=(a+b+c)/2
    return "Area is : ",math.sqrt(s*(s-a)*(s-b)*(s-c))  

  def areatriangle5(self):
    a=int(input("Side is : "))
    return (math.sqrt(3)/4)*a*a
  
  def areatriangle6(self):
    b=int(input("Base is : "))
    a=int(input("Altitude is : "))
    return "Area is : ",0.5*b*a
  
  def areatriangle7(self):
    b=int(input("Base is : "))
    h=int(input("Height is : "))
    return "Area is : ",0.5*b*h

class parallelogram(shape):
  def areaparallelogram(self):
    a=int(input("Side is : "))
    h=int(input("Height is : "))
    return "Area is : ",a*h

class rhombus(shape):
  def arearhombus(self):
    d1=int(input("One Diameter is : "))
    d2=int(input("Second Diameter is : "))
    return "Area is : ",0.5*d1*d2

class trapezium(shape):
  def areatrapezium(self):
    h=int(input("Height is : "))
    a=int(input("One parallel side is : "))
    b=int(input("Another parallel side is : "))
    return "Area is : ",0.5*h*(a+b)

class semicircle(shape):
  def areasemicircle(self):
    r = int(input("Radius is : "))
    return "Area is : ",0.5*(22/7)*r*r
  
class sector(shape):
  def areasectorcircle(self):
    r = int(input("Radius is : "))
    ang = int(input("Angle is : "))
    return (22/7)*r*r*(ang/360)

class cuboid(shape):
  def areacuboid(self):
    l=int(input("Lenght is : "))
    b=int(input("Breadth is : "))
    h=int(input("Height is : "))
    return "CSA is : ",2*h*(l+b)," and TSA is : ",2*((l*b)+(b*h)+(h*l))," And Volume is : ",l*b*h

class cube(shape):
  def areacube(self):
    a=int(input("Side is : "))
    return "CSA is : ",4*a*a," and TSA is : ",6*a*a," and Volume is : ",a*a*a

class prism(shape):
  def areaprism(self):
    bl=int(input("Base lenght is : "))
    bb=int(input("Base width is : "))
    bp=2*(bl+bb)
    h=int(input("Height is : "))
    lsa = bp*h
    tsa = lsa + 2*(0.5*bb*h)
    return "CSA is : ",lsa," And TSA is : ",tsa," And Volume is : ",bl*bb*h

class Cylinder(shape):
  def areaCylinder(self):
    r=int(input("Radius is : "))
    h=int(input("Height is : "))
    return "CSA is : ",2*pi*r*h," and TSA is : ",2*pi*r*(r+h)," and Volume is : ",pi*r*r*h

class Cone(shape):
  def areaCone(self):
    r=int(input("Radius is : "))
    h=int(input("Height is : "))
    l=math.sqrt(r*r+h*h)
    return "CSA is : ",pi*r*l," and TSA is : ",pi*r*(r+l)," and Volume is : ",(pi*r*r*h)/3

class Sphere(shape):
  def areaSphere(self):
    r=int(input("Radius is : "))
    return "CSA and TSA is : ",4*pi*r*r," and Volume is : ",(4*pi*r*r*r)/3

class Hemisphere(shape):
  def areaHemisphere(self):
    r=int(input("Radius is : "))
    return "CSA is : ",2*pi*r*r," and TSA is : ",3*pi*r*r," and Volume is : ",(2*pi*r*r*r)/3

while(True):   
  print("your figure is : \n1) 2-D \n2) 3-D")
  ch=int(input("Figure Type Number : "))
  if ch==1:
    print("Choose number for area calculation of the shapes : \n1) Circle \n2) Rectangle \n3) Square \n4) Triangle with three side \n5) Equilatrel Triangle \n6) Triangle with base and altitude \n7) Triangle with base and height in Right Angle \n8) Parallelogram \n9) Rhombus \n10) Trapezium \n11) Semi-Circle \n12) Sector of circle")
    ch2=int(input("Enter Figure Number : "))
    if ch2==1:
      circle=Circle()
      print(circle.areacircle())
    elif ch2==2:
      rectangle=rectangle()
      print(rectangle.arearectangle())
    elif ch2==3:
      square=square()
      print(square.areasquare())
    elif ch2==4:
      triangle = triangle()
      print(triangle.areatriangle4())
    elif ch2==5:
      triangle = triangle()
      print(triangle.areatriangle5())
    elif ch2==6:
      triangle = triangle()
      print(triangle.areatriangle6())
    elif ch2==7:
      triangle = triangle()
      print(triangle.areatriangle7())
    elif ch2==8:
      parallelogram = parallelogram()
      print(parallelogram.areaparallelogram())
    elif ch2==9:
      rhombus = rhombus()
      print(rhombus.arearhombus())
    elif ch2==10:
      trapezium = trapezium()
      print(trapezium.areatrapezium())
    elif ch2==11:
      semicircle = semicircle()
      print(semicircle.areasemicircle())
    elif ch2==12:
      sector = sector()
      print(sector.areasectorcircle())
    else:
      print("Wrong Choice ... ")
  elif ch==2:
    print("Choose number for area calculation of the shapes : \n1) Cuboid \n2) Cube \n3) Prism \n4) Cylinder \n5) Cone \n6) Sphere \n7) Hemisphere ")
    ch3=int(input("Enter Figure Number : "))
    if ch3==1:
      cuboid = cuboid()
      print(cuboid.areacuboid())
    elif ch3==2:
      cube = cube()
      print(cube.areacube())
    elif ch3==3:
      prism = prism()
      print(prism.areaprism())
    elif ch3==4:
      Cylinder = Cylinder()
      print(Cylinder.areaCylinder())
    elif ch3==5:
      Cone = Cone()
      print(Cone.areaCone())
    elif ch3==6:
      Sphere = Sphere()
      print(Sphere.areaSphere())
    elif ch3==7:
      Hemisphere = Hemisphere()
      print(Hemisphere.areaHemisphere())
    else:
      print("Wrong Choice ... ")
  else:
      print("Wrong Choice ... ")
  
