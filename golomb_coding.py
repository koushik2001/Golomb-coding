import math
n=int(input("enter the value of n"))
m=int(input("enter the value of m"))

def golomb_coding(n,m):
    a=math.floor(math.log(m,2))
    b=math.ceil(math.log(m,2))
    p=math.log(m,2)
    q=math.floor(n/m)
    r=n-q*m
    def power(k):
        global u
        if(k%2==0):
            if(k/2==1):
                u=1
            else:
                power(k/2)
        else:
            u=0
    power(m)
    def decimalToBinary(n):
        global j
        j=bin(n).replace("0b", "") 

    def unary():
        if(q==0):
            print("golomb_code:",end="")
            print('1',end="")
        else:
            print("golomb_code:",end="")
            for i in range(q):
                print('0',end="")
            print('1',end="")
    unary()

    if(u==1):
        decimalToBinary(r)
        global j
        if(len(j)<p):
            for v in range(int(p-len(j))):
                r='0'+j
                j=r 
            print(r)

        elif(len(j)==p):
            r=j
            print(r)

    z=pow(2,math.ceil(p))-m

    if(u==0):
        for f in range(z):
            if(r==f):
                decimalToBinary(r)
                if(len(j)<a):
                    for v in range(int(a-len(j))):
                        r='0'+j
                        j=r 
                    print(r)
                elif(len(j)==a):
                    r=j
                    print(r)
        for f in range(z,m):
            if(r==f):
                decimalToBinary(r+z)
                if(len(j)<b):
                    for v in range(int(b-len(j))):
                        r='0'+j
                        j=r 
                    print(r)
                elif(len(j)==b):
                    r=j
                    print(r)

golomb_coding(n,m)
        
