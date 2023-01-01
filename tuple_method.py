# Convert a tuple into a list

contries = ("India","Russia","Germany")
# temp = list(contries);
# Convert a tuple into a list
# temp.append("Singapore")
# print(temp)

# temp.pop(2);
# pop(ind) --> this function is used to poped out value/items present at a index ind 
# print(temp)

# contries = tuple(temp);
# print("After modifying tuple element :");
# print(contries)

contries2 = ("Itely",);

# TUple can be concatinate

newcontries = contries+contries2;
print(newcontries);

num =(2,3,5,31,3,1,4);
print(num);
res =num.index(3,2,5);
# when we find index of any element in a particular rage then we use this syntax --> num,index(ele, start, end);
# It will search from start to till end-1 index
print(res);

print(num.count(3))
# used to print the count of any element --> count(ele);

nation1 = "India";
nation2 = "Russia";
print(nation1+nation2)
