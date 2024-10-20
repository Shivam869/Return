def recur_factorial(num):
    if num==1:
        return num
    else:
        return num*recur_factorial(num-1)
num=int(input("Enter a number:"))
if num<0:
    print("Sorry factorial does not exist for negetive numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("factorial of",num,"is",num*recur_factorial(num))

  