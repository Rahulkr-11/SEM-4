#WAP whether the given number is even or not

def check(x):
    if x==0:
        print ("Invalid Number ")
    else: 
        if x%2==0:
            print ("The given number is even")
        else:
            print ("The given number is NOT even")


x=int (input("Enter your number : "))
check(x)