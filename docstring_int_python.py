# Docstring is a special type of string used to demonstrate programmer about the work facilities of any function 
# and many more it is like comment but it can not be ignored,

def square(n):
    '''This function takes input an integer and returns an square value''';

    print(n**2);
    # '''This function takes input an integer and returns an square value''';
square(5);
print(square.__doc__); # this is the syntax is used to print DOcstring written inside function indentation

# Docstring must be written just bellow the function name
# Other wise Python interpreter shows None;