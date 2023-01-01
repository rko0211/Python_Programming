# Every things in python are basically Objects
# When user give input manually then it's data type become String or str data type

# Match case statement is similler with Switch case statement in C/C++

# Syntax of match case statement
# a is the varible to match
a = int(input("Enter the number : "))
match a:     # Comparing the variable with all the pattern
    case 0:
        print("Match case is 0");
        # No break statement is required here
    case 1:
        print("Match case is 1");
        # Inside the case we can use If, Else statement
    
    case _:
        print("Default case")
