def bubble_sort(alist):
    for passnum in range(len(alist)):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp

def main():
    alist=list()
    num=input("Enter num of element:")
    for i in range(int(num)):
        n=input("Enter num:")
        alist.append(int(n))
    print("The Unsorted array:",alist)
    bubble_sort(alist)
    print("Sorted array:",alist)
    
if __name__=="__main__": main()
        
    