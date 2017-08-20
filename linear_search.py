
def linear_search(num,search):
    for i in range(int(len(num))):
        if num[i]==int(search):
            print("Number found at {} index".format(i))
            exit
    
    print("number not found")
        
def main():
    num=list()
    n=input("Enter no of element")
    for i in range(int(n)):
        number=input("Enter number")
        num.append(int(number))
    search=input("Enter number to search")
    linear_search(num,search)
    

if __name__ == '__main__':main()

