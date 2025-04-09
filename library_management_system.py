class library:
  def __init__(self,roll_no,name):
    self.roll_no = roll_no
    self.name = name
    self.a={}
    self.b={}
    self.c={}

  def addbook(self):
    bn=input("Enter the book name : ")
    bid=int(input("Book Id : "))
    self.a[bn]=bid
    return "Book Added successfully ..."
  
  def book_details(self,ch1):
    if ch1==1:
      return self.a
    elif ch1==2:
      return self.c

  def removebook(self):
    bn=input("Enter the book name : ")
    if bn in self.a:
      del self.a[bn]
    return "Book is Removed from Database . "

  def addmember(self):
    name = input("Name of the Member : ")
    roll_no = int(input("Roll Number of the member : "))
    self.b[roll_no]=name
    return "New Member added successfully ..."
  
  def removemember(self):
    roll_no = int(input("Roll Number of the member : "))
    if roll_no in self.b:
      del self.b[roll_no]
    return "Member is removed successfully ..."

  def member_lib(self):
    name = self.name
    roll_no = self.roll_no
    self.b[roll_no]=name
    return self.b

  def transaction(self):
    r=int(input("Enter your roll No : "))
    if r in self.b:
      print("Enter choice : \n1.Borrowing \n2.Returning")
      ch=int(input("enter choice :"))
      if ch==1:
        bn=input("Enter book name : ")
        bid=int(input("Enter Book id : "))
        if bn in self.a:
          self.c[bn]=bid
          return ("Book is Borrow ...")
        else:
          return "Book is no found"
      elif ch==2:
        bn=input("Enter the book name : ")
        bid=int(input("Book Id : "))
        del self.c[bn]
        return ("Book is returning ....")
    else:
      return ("You are Not a member ...")
roll=int(input("Admin id : "))
admin=input("Admin name : ")
a=library(roll,admin)
while(True):
  print("Enter your choice : \n1.Member Record \n2.Book Record \n3.Last Entry \n4.Add New Book \n5.Remove Book \n6.Add New Member \n7.Remove Member")
  ch=int(input("Enter choice number : "))
  if ch==1:
    print("Member details",a.member_lib())
  elif ch==2:
    print("Enter your choice : \n1.Total Book details \n2.Present Borrowed Book record")
    ch1=int(input("Enter book record number : "))
    if ch1==1:
      print("Books details : ",a.book_details(ch1))
    elif ch==2:
      print("Book details : ",a.book_details(ch1))
  elif ch==3:
    print("Book transaction ",a.transaction())
  elif ch==4:
    print("Adding New Book : ",a.addbook())
  elif ch==5:
    print("Removing Book : ",a.removebook())
  elif ch==6:
    print("Add New Memeber : ",a.addmember())
  elif ch==7:
    print("Removing Member : ",a.removemember())
  else: 
    print("Wrong Choice ...")
