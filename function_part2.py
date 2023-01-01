# Default arguments
# When ever we define any fuction then we have to use "def" key words
def calcaverage(a=1,b=3):
    print("The average is :",(a+b)/2)
    print("The value of a and b is ",a,b)

calcaverage()
calcaverage(2,4)
calcaverage(4)
calcaverage(b=2, a=3)  # In this, case order of arguments does not matter
calcaverage(b=4,a=2)

# Variable length arguments
def average(*number):       #*number-> By doing this we actually say number variable can store list of number
    type(number);
    sum=0;
    for i in number:

        sum = sum+i;
    
     
    return (sum/len(number));



c = average(5,6);
print("The average is",c);
