t = int(input("Enter the time :"))
if(t>4 and t<=10):
    print("Good Morning");
elif(t==12):
    print("Good Noon");

elif(t>12 and t<6):
    print("Good After noon")

elif(t>=6 and t<7):
    print("Good Evening")
else:
    print("Good Night")