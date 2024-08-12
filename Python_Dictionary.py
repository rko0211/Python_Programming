# Dictionary in python is the combination of key-value pair 
# it is a special type of object in python used to store kay-value pair

# dictionary is a ordered collection of kay-value pair

# item = (key+value)

dict= {
    'name' : "Rahul",
    "name":"raja",   #in this line value associated with key 'name' is updated
     "age":20, 
     "eligible" : True
}

print(type(dict));
print(dict);
print(dict["eligible"]);

ep1={
    121:20,132:40,133:50,135:6
};
ep2={
    111:63,222:45,232:34
};
# Update function is used to update any dictionary by appending other dictionary items;

ep1.update(ep2);
print(ep1);
ep1.popitem();
print(ep1)
# x = ep2.pop(232);
del ep2[232]
# print(x);
print(ep2);
