def Fibinocci(N):
    if N<0:
        print ("Invalid Input")
    elif N==0:
        return 0
    elif N==1:
        return 1
    return Fibinocci(N-1)+Fibinocci(N-2)

N=int(input("Enter a Number : "))
print("Fibinocci of ",N,"is :",Fibinocci(N))