class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
  def insertatbegin(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      return
    else:
      new_node.next=self.head
      self.next=new_node
  def insertatindex(self,data,index):
    if (index==0):
      self.insertatbegin(data)
      return 
    pos=0
    current_node=self.head
    while(current_node!=None and pos!=0):
      pos=pos+1
      current_node=current_node.next
    if current_node!= None:
      new_node=Node(data)
      new_node.next=current_node.next
      current_node.next=new_node
    else:
      print("index not found ")
  def insertatend(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      return
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    current_node.next = new_node
  def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

a=linkedlist()
a.insertatbegin("keshav")
a.insertatindex("rana",1)
a.insertatend("rajput")
a.printLL()