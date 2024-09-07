a = input("Enter operation (or, and, not, xor) ");

if(a=="or"):

  print("Enter 2 value ");
  n1 = int(input());
  n2 = int(input());
  print("Result of OR(|) operator is: ",( n1|n2));
elif(a=="and"):
  print("Enter 2 value ");
  n1 = int(input());
  n2 = int(input());
  print("Result of AND(&) operator is: ",( n1&n2));

elif(a=="xor"):
  print("Enter 2 value ");
  n1 = int(input());
  n2 = int(input());
  print("Result of XOR(^) operator is: ",( n1^n2));

else:
  print("Enter 1 value ");
  n1 = int(input());
  print("Result of NOT(~) operator is: ",( ~n1));









