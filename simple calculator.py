print("Simple calculator")
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))    

print("Sum:", a + b)
print(" Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)

else:
    print("cannot divide by zero")

print( "Percentage:", a % b)
print ("Power:", a ** b)