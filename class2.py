class myclass2:
  # these are class or instanteneous attributes
  name = "Prakash Mondal"
  language = "py"
  salary = 12000000


instance_of_myClass2 = myclass2();

instance_of_myClass2.experience = 1;  # here "experience" is instance attribute or object attribute 

instance_of_myClass2.language = "js";  # instance attribute has higher priority than class attribute

# First python search the attribute in object or instance level if it does not present there then it goes to class level, if there also it is not present then it is assigned to class level.


print(instance_of_myClass2.name, instance_of_myClass2.language, instance_of_myClass2.salary, instance_of_myClass2.experience);
