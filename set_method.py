cities1 = {"Delhi","Mumbai","Kolkata","Tokeyo"};
cities2 ={"Kanpur","Maddras","Kharagpur","Tokeyo"};

# c1.union(c2)--> is used to merge two set
print(cities1.union(cities2)); 

# If we want to see common element between two set
# THen we use c1.intersection(c1);

print(cities2.intersection(cities1));

# add function is used to add new element to the set

cities1.add("Bangalor");

print(cities1);

s1 ={1,3,5};
s2 ={1,3,4};

# Symmetric_difference
print(s1.symmetric_difference(s2));

# if we want to print element that is present only in s1 not in s2 then we use difference method

print(s1.difference(s2));

# if we want to add new element that present in set1 , s1 and not present in set2, s2
# Then we use update function

# s2.update(s1);

print(s2);   # print {1,3,4,5} or in different order


# If we want to delete or remove particular element from set then we use remove()/discard()
# function

# s2.remove(5)
# s2.discard(5);

# discard() fun will not through error if the element is not present inside the set
# Where as remove() function will through the error if element is not present inside the set

print(s2);

# del key word is used to delete any set

del s2;

# pop() function is used to pop element from set
item = s1.pop()

print(item);