# Bydefault python takes input from USER as a string / Python interpretor is not so inteligent that can differentiate 
# between string and number bydefault it conscider as it is  a string
# We have to typecast this value;

# ...................................................................................................................

# print("Enter the value here :")

# n =int(input("Enter the value here : "));
# print("My name is :",n);
# print("Type of n is :",type(n));

a =input("Enter first input : ")
b =input("Enter second input : ")
print(a+b)
print(int(a)+int(b))
# Type casting of a in to integer -> int(a)