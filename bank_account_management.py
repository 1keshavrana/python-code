class bank:
  def __init__(self,account_no,intial_amt):
    self.account_no = account_no
    self.inital_amt = intial_amt
  def current_balance(self):
    return self.inital_amt
  def deposit(self):
    a=int(input("Amount Deposit : "))
    self.inital_amt = self.inital_amt + a
    return (self.inital_amt)
  def withdrawal(self):
    a=int(input("Amount Withdrawal : "))
    self.inital_amt = self.inital_amt - a
    return (self.inital_amt)
ac=int(input("Enter your Account number - "))
amt= int(input("Enter inital Balance - "))
a = bank(ac,amt)
print("1. Current Balance \n2. Deposit \n3. Withdrawal ")
c=1
while(c==1):
  i=int(input("Enter your choice : "))
  if i==1:
    print("Account Number : ",ac,"\nBalance : ",a.current_balance())
  elif i==2:
    print("Account Number : ",ac,"\nUpdate Amount : ",a.deposit(),"Successful...") 
  elif i==3:
    print("Account Number : ",ac,"\nUpdate Amount : ",a.withdrawal(),"Successful...") 
  else:
    print("wrong choice !!! ")
  c=int(input("Enter 1 for more modification : "))