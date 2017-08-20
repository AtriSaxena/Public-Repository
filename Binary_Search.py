
def binary_search(alist,sear):
    start=0
    end=len(alist)-1
    while start<=end:
        midpt=(start+end)/2
        if alist[midpt]==sear:
            return midpt
        elif alist[midpt]<sear:
            start=midpt+1
        else:
            end=midpt-1
            
    return -1
    
    
    
    
def main():
    alist=list()
    num=input("Enter number of element")
    for i in range(int(num)):
        n=input("enter number:")
        alist.append(int(n))
    sear=int(input("Enter number to seach:"))
    index=int(binary_search(alist,sear))
    if index==-1:
        print("Number {} not found in array".format(sear))
    else:
        print("Number {} found at index {}".format(sear,index))
    
    
if __name__=="__main__":main()
