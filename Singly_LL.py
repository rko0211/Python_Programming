class Node:
  # This helps to create Node
  def __init__(self,data=None, next=None):
    self.data = data;
    self.next = next;
  

class SLL: 
  # this refers to the current instance. 'self' is same as 'this' 
  def __init__(self,start=None):
    self.start = start;
    
  
  def is_empty(self):
    return self.start==None;
  
  def inserAtfirst(self,data):
    nodecreate = Node(data);
    if not self.is_empty():  # Not empty 
      temp = self.start;
     
      nodecreate.next = temp;
      self.start = nodecreate;


  def insertNode(self,data):
    # Node created that will be inserted into the list
    node = Node(data);
    if not self.is_empty():#is_empty is an instantaneous method hence we need the instance to call it
      temp = self.start;
      
      while temp.next!=None:
        temp = temp.next;
      
      temp.next = node;

    else:
      self.start = node;

  def displayNode(self):
    temp = self.start;
    self.x = 10;
    while temp!=None:  # when temp points to the NULL then stop the iteration
      print(temp.data, end=" ");
      temp = temp.next;

  def deleteNode(self,data):
    temp = self.start;
    prev = None;
    while temp!=None:
      if(temp.data==data):
        break; 
      prev = temp;
      temp = temp.next;
    
    if(temp is not None):
      if(prev !=None):
        prev.next = temp.next;
        # In python due MM technique, Now automatically memory will be free 
      else:
        self.start = temp.next;
    else:
      print(f"we are sorry, but {data} is not present in the list")

      

     

obj = SLL();
obj.insertNode(1);
obj.insertNode(2);
obj.insertNode(3);
obj.insertNode(4);
obj.insertNode(5);
obj.inserAtfirst(0);
obj.insertNode(6);
obj.deleteNode(3)
obj.displayNode();

print("");
print(obj.x);

  