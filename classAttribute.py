class myclass6:
  pay_rate = 0.8;  # class attribute 


instance_of_myclass6 = myclass6();
print(myclass6.pay_rate);
print(instance_of_myclass6.pay_rate);

instance_of_myclass6.value = 100; # value is instance level attribute

# print(myclass6.value); # error using clss name we can to access instance level attributes
print(instance_of_myclass6.value);


print("Class level attributes: ");
print(myclass6.__dict__);  # print all class level attributes
print();
print("Instance/Object level attributes: ");
print(instance_of_myclass6.__dict__);  #print all instance level attributes         