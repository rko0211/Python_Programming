class myclass3:
  # name = "Prakash Mondal"
  def getInfo(self):
    # self parameter itself is an object or instance of this class, myClass3 which is instance_of_myClass3
    
    print(f"Good afternoon every one my name is {self.name}");


instance_of_myClass3 = myclass3();
instance_of_myClass3.name = "Prakash Mondal"; # as this attribute is not there in the class so it is set there as a class attribute.


# instance_of_myClass3.getInfo(); is same as myclass3.getInfo(instance_of_myClass3);

# myclass3.getInfo(instance_of_myClass3)

instance_of_myClass3.getInfo();

# the instance by which any class method is called that same instance is also bydefault send as a argumentsin that method, so we have tho receive that instance there as a parameter otherwise it will show error.


print(instance_of_myClass3);
