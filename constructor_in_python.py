class myClass4 :
  def __init__(self, a,b,c):
    print("Hello");
    (self.f())
  def f(self):
    print("world");
    # Implicitly return "None" by the function 


# when object is created or instanciated then a magic method is called it is known as constructor;
instance_of_myClass4 = myClass4(1,2,3);
# print(int);

instance_of_myClass4.f="jjwel"; # you assign a string "jjwel" to instance_of_myClass4.f, replacing the method "f" with this string

# instance_of_myClass4.f();  # Now "f" is a string and str object are not cllble

print(instance_of_myClass4.f);

# In python memory is allocated to the value not to the variable which make the memory management process more efficient