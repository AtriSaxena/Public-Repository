#wrong answer
def Quick_sort1(num):
    less=[]
    equal=[]
    greater=[]
    if len(num)>1:
        pivot=num[0]
        for x in num:
            if x>pivot:
                less.append(x)
            if x==pivot:
                equal.append(x)
            if x<pivot:
                greater.append(x)
        return Quick_sort1(less)+equal+Quick_sort1(greater)
    else:
        return num

num=list()
n=int(input("Enter size of list"))
for i in range(n):
    dig=input("Enter number")
    num.append(int(dig))
high=int(len(num))
low=0
Quick_sort1(num)
print("Sorted list {}".format(num))                    