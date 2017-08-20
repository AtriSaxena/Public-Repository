def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b, end=' ')
        a,b = b,a+b
    
def main():
    n=input("Enter number:")
    fibonacci(int(n))
        
if __name__=="__main__":main()