def Selection_sort(arr):
    for i in range(len(arr)):
        minpos=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minpos]:
                minpos=j
        temp=arr[i]
        arr[i]=arr[minpos]
        arr[minpos]=temp

arr=list()            
n=int(input("Enter size of list"))
for i in range(n):
    dig=input("Enter number")
    arr.append(int(dig))
Selection_sort(arr)
print("Sorted list {}".format(arr))            
    