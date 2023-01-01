# List is a collection of many data item's of similer or disimiler data type 

l =[3,2,1,5,"Prakash",'rahul',6];   #Decleration of list

print("Length of the list is :",len(l));
# List index started from 0
for i in l:
    print(i);

# List are mutable that means we can change list item at any possition
print("After changing list items :");
l[0]=11;
l[5]="Shreya";
l[6]="Disha";
print("Length of the list is :",len(l));
for i in l:
    print(i);

print("Individual list item :",l[len(l)-1]);

# l[-1] is same as l[len(l)-1];
# l[-3] is same as l[len(l)-3];