list =[1,4,6,2,7,3,2];
print("Type of list: ",type(list));
# print("Before append, list looks like :");
# for i in list:
#     print(i);

# print("After append 8 in the list it looks like :");

# list.append(8);
# for i in list:
#     print(i);

# list.sort();  # List items would be sorted in Ascending order 

# print(list);
# list.sort(reverse=True)  # List item's would be sorted in Descending order
# print(list);

# This function is used to reverse the original list
# list.reverse() 
# print(list);

# The bellow function is used to return the index of the first occurance of any element present inside the list
print(list.index(2));   # It will print index of 2, here that is 3;

# Count function return the number that is how many times any particular elements present inside the list

print(list.count(2));

# m=list;
# Here m is the refferance of the list not a copy value if we change m then it will reflect to the original list
# m[0]=0;
# print(list)

# m = list.copy(); 
# Now original list will not be affected if we change m because one copy of the list is created and which is stored in m
# m[0]=0;
# print(list);

# list.insert(1,899);
# list.insert(ind,val) is used to insert any value at any particular index of the list
# print(list)

m=[900,1000,2000];
# list.extend(m);
# print(m);
# print(list)
# List concatination mathod

k = m+list;
print(k);
k = list+m;
print(k);