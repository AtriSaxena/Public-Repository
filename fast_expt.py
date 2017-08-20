
def fast_exp(num,pow):
    if int(pow)==0:
        return 0
    elif int(pow)==1:
        return num
    else: 
        y=fast_exp(num, int(pow)/2)
        if int(pow) % 2 ==0:
                    return int(y) * int(y)
        else:
            return int(num)* int(y)* int(y)
        

def main():
    number=input("Enter number")
    pow=input("Enter power")
    ans=fast_exp(number,pow)
    print("Exponential is {}".format(int(ans)))


if __name__=='__main__':main()
    