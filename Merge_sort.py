

def Merge_sort(low,high ):
    if low < high:
        mid=int((low+ high)/2)
        #print(mid)
        Merge_sort(low,mid)
        Merge_sort(mid+1, high-1)
        Merge(low,mid,high-1)

def Merge(low,mid,high):
    i=low
    j=mid+1
    k=low
    while i<=mid and j<= high:
        if num[i]<= num[j]:
            sort.append(num[i])
            i=i+1
        else:
            sort.append(num[j])
            j=j+1
        k=k+1
    print(sort)    
    if i > mid:
        for j in range(j,high):
            sort.append(num[j])
    else:
        for i in range(i,mid):
            sort.append(num[i])                      

                
num=list()
sort=list() 
n=int(input("Enter size of list"))
for i in range(n):
    dig=input("Enter number")
    num.append(int(dig))
high=int(len(num))
low=0
Merge_sort(low, high)
print("Sorted list {}".format(sort))       