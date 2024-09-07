class Node:
  def __init__(self,prev=None, data=None, next=None):
    self.prev = prev; # self.prev is an instanteneous variable where as prev is an local variable
    self.data = data;
    self.next = next;
  
class DLL:
  def __init__(self,start=None):
    self.start = start;
  
  def is_empty(self):
    return self.start==None;
  
  def insertNode(self,data):
    node = Node(None,data,None);
    if not self.is_empty():  # Not empty
      temp = self.start;
      while temp.next is not None:
        temp = temp.next;
      
      node.prev = temp;
      temp.next = node;

    else:
      self.start = node;


  def insertAfter(self,data,element):
    temp = self.start;
    if self.is_empty():
      print("List is empty! Please enter some element");
    else:
      while temp !=None:
        if(temp.data==data):
          break;
        temp = temp.next;
      if(temp==None):
        print("Element does not present in the list");
        return;
      node = Node(temp.prev,element,temp.next)
      temp.prev.next = node;
  def displayList(self):

      temp = self.start;
      while temp is not None:
        print(temp.data, end=" ");
        temp = temp.next;



obj = DLL();

obj.insertNode(1);
obj.insertNode(2);
obj.insertNode(3);
obj.insertNode(4);
obj.insertNode(5);
obj.insertAfter(2,6);
obj.displayList();
print();