# Break Statement is used to go out of the loop
# The bellow for loop will print 1 to 5 
print("Break statement using for loop :");
for i in range(1,10):
    if i==6:
        break;
    print(i);

print("Break statement using while loop :");
# While loop will print from 1 to 4
i =1;
while(i<=10):
    if(i==5):
        break;
    print(i);
    i=i+1;

# Continue statement is used to skip to the next iteration

print("Continue statement using for loop :");
# This for loop will print all i from 1 to 10 except 5
for i in range(1,10):
    if(i==5):
        continue;
    print(i);


