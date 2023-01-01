# Tuple is just similer like list
# Only difference between list and tuple is that tuple is immutable where as list is mutable
# Immutable means tuple items or value can't be changed  or we can say tuple's are unchangeable
# We can convert tuple in to list then we can change those value or items
# Tuple length can not be changes by using insert or append function
# Declearation of tuple
tup =(4,3,1,"prakash",'mondal');

print(type(tup));
# Indexing in tuple same as like list
print("Length of the tuple is :",len(tup))
print(tup);
print(tup[3])
# tup[4]="subham";   --> It will show error because tuple are immutable

tup2 = tup[1:4];
print(tup2)
