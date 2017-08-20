
def Quick_sort(num,low,high):
    if low < high: 
        j=partition(num,low,high)
        Quick_sort(num,low,j-1)
        Quick_sort(num, j+1, high)
        

def partition(num,low,high):
    i=int(low+1)
    j=high 
    x=num[low]
    done=False
    while not done: 
        while i <= j and num[i]<= x:
            i=i+1
        while i <= j and num[j]>= x:
            j=j-1
        if i < j:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
        elif i > j:
            done=True
    temp=num[low]
    num[low]=num[j]
    num[j]=temp 
    return j

num=list()
n=int(input("Enter size of list"))
for i in range(n):
    dig=input("Enter number")
    num.append(int(dig))
high=int(len(num))
low=0
Quick_sort(num, low, high-1)
print("Sorted list {}".format(num))                    