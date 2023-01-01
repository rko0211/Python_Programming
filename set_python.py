# Every thing in python are object like every data structure or container in are objects
 
# Set is a special type of object in python that store only unique element


# set is a collection of well define objects
# declearation of sets

s = {2,4,2,6};

# Set is a unordered collection of data items --> order is not be maintaioned by python 
# interpretor in set

# set donot contains duplicate , sets are un-changeable or immutatble like tuple while 
# creating items

# We can not access element through index

print(s);  # print 2,4,6 or in different order

info ={"Prakash",1.23,1,3,2,False}  #--> it is a set

# We can print set element by  loop

print(info)

for val in info:
    print(val)


prakash ={};
print(type(prakash));   #--> It will show Dictionary class rather set class

hello = set() #-> Syntax to declear empty set

print(type(hello));