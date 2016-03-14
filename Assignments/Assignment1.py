n = int(input("Enter a number to test the implemented functions: "))

# fibonacci using recursion
def fibonacci(n):
    if(n == 0 or n==1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    if(n == 1):
        return False
    for i in range(2,n-1):
        if(n % i == 0):
            return False
    return True

# fibonacci using generators
def fib(n):
    a, b = 1 ,2

    for _ in range(n):
        yield a
        a, b = b, a+b

print ("Fibonacci of %d is %s" %(n ,fibonacci(n)))
print ("-------------------------------------")
print ("Fibonacci of %s using generators: " %n)
print (str(list(fib(n)))[1:-1])
print ("-------------------------------------")
print ("Fibonacci of %s using generators: " %n)
for i in fib(n):
    print (i)
print ("-------------------------------------")
print ("Check if %d is prime number : %s" %(n,is_prime(n)))
print ("-------------------------------------")
