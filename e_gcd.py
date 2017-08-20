
def gcd1(num1,num2):
    if num2==0:
        return num1
    else:
        return gcd1(num2,num1%num2)
    
        
num1 = int(input("Enter number to find GCD"))
num2 = int(input("Enter number to find GCD"))
ans=gcd1(num1,num2)
print("GCD is {}".format(ans))