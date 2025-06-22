
def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))
    
n=int(input("enter a number")) #input from user

result=factorial(n)
print("The factorial of", n ,"is",result)
