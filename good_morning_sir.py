import time
t= time.strftime('%H:%M:%S');
# Initially all inputs or value in python are in Str class or they are string
# print(type(timestamp))
# print(timestamp)

# hour = int(time.strftime('%H'));\
hour = int(input("Enter Hour :"));

print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!");

elif(hour>=12 and hour<=17):
    print("Good Afternoon Sir!");

elif(hour>17):
    print("Good Night Sir!");
