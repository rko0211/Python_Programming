class myclass5:
  def __init__(self, name:str ,lang, price):
    assert price>=0,f"{price} should be greater than or equal to 0";
    # second argument is the console message incase of error

    print("Hello, I am constructor");

    self.name = name  ; # left side is instance or class variable and right sides are local varible
    self.language = lang;
    self.price = price;


# instance_of_myclass5 = myclass5("Prakash Mondal","py", -1); error due to negative price

instance_of_myclass5 = myclass5("Prakash Mondal","py", 1);  # OK


print(instance_of_myclass5.name, end=" ");

print(instance_of_myclass5.language);
