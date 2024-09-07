
f = open("text.txt");  # By-default Read operation
# data = f.read()
# print(data);

lines = f.readlines();
print(lines, type(lines));

# line1   = f.readline(); -> 1st line read and control goes to 2nd line 
# print("1 ", line1, type(line1));

# line2 = f.readline()   -> 2nd line read and control goes to 3rd line  
# print("2 ", line2, type(line2));

# line3 = f.readline();
# print("3 ", line3, type(line3));

# line4 = f.readline();
# print("4 ", line4, type(line4));


line5 = f.readline();
print("5 ", line5, type(line5));
print(line5=="");

f.close();

# st = " Hello World"
# f1 = open("text1.txt","a");
# f1.write(st);
# f1.write(st);
# f1.close();


f2 = open("text1.txt","w");

f2.write("kjdskjdkd")

f2.write("kjdskjdkd1222222222222222222")
f2.writable();
f2.close();