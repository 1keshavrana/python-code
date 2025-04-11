class employee:
  def __init__(self):
    self.member={}
    self.department={}
    self.salary={}
  
  def addemployee(self):
    name=input("Enter the Name of the Employee : ")
    Eid=int(input("Enter the employee id : "))
    self.member[Eid]=name
    self.departmentadd()
    return "Member Added successfully ..."
  
  def removeemployee(self):
    Eid=int(input("Enter the employe id : "))
    if Eid in self.member:
      del self.member[Eid]
      return "Employe Data is Deleted ..."
    else: 
      return "Employe is Not found ..."
  def employe_data(self):
    return self.member
    
  def departmentadd(self):
    Eid=int(input("Enter the Employe id : "))
    if Eid in self.member:
      dep=input("Enter your department : ")
      self.department[Eid]=dep
      return "Department is updated."
    else:
      return "Employe is not found."
  def depart_data(self):
    return self.department
  
  def salaryadd(self):
    Eid=int(input("Enter the Employe id : "))
    if Eid in self.member:
      amt=int(input("Enter the amount : "))
      if Eid in self.salary:
        last_sal=self.salary[Eid]
        self.salary[Eid]= last_sal + amt
        return "Salary Deposit ..."
      else:
        self.salary[Eid]= amt
        return "Salary Deposit ..."
    else:
      return "Employe Not found ..."

  def salarydata(self):
    return self.salary

a=employee()
print("Enter your Choice : \n1.Add Employee \n2.Remove Employee \n3.Employe Details \n4.Department Details \n5.Deposit Salary \n6.Salary details")
while(True):
  ch=int(input("Enter choice number : "))
  if ch==1:
    print(a.addemployee())
    #a.departmentadd()
    print("Member Added Successfully ...")
  elif ch==2:
    print(a.removeemployee())
  elif ch==3:
    print("Employee Details : ",a.employe_data())
  elif ch==4:
    print("Department Details : ",a.depart_data())
  elif ch==5:
    print(a.salaryadd())
  elif ch==6:
    print("Salary Details : ",a.salarydata())
  else:
    print("Not valid choice ...")
