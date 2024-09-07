#Strings are immutable

name ="Prakash"

print(len(name));
print(len("name"))

# name.upper() this function will return a new string 
# never changes the original string
print(name)
name = name.upper();
print(name)
print(name.lower());
# That means string1 will not be converted in to lower or upper case rather it will generate a new string.
# Those function will not change the existing string.
a ="prakash !!!!!!!!! prakash";
# a.rstrip() -> function is used to strip trailing charecters , it will not strip leading charecter

print(a.rstrip("!"));

print(a.replace("P","A"));

print(a.split(" "));

# capitalize() function turns first charecter of a string into capital alphabates 
print(a.capitalize());

heading = "Wellcome to the console!";
print(len(heading))
print((heading.center(50)));
print(len(heading.center(50)));

print(heading.istitle());




