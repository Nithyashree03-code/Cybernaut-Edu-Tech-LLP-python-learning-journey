def  gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
output =gcd(a,b)
print("Greatest Common Divisor is: ")
print(output)