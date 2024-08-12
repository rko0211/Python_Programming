txt = "Hello, my name is {1}, i am from {0}";

name ="Prakash";
country = "India";
print(txt.format(country, name));   
# txt.format() is a string method used to formate string
txt1 = "Hello, my name is {}, i am from {}";
print(txt1.format(country, name));   


# Using fstring we can use variable inside a string 

price =28.896678;
txt2 = f"The price of this value is {price:.2f}"    # syntax of the f string 
print(txt2)

ff = 10;
t = f"hello {ff}";
print(t);

