def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
for num in fibonacci(10):
    print(num)
    
print("\nUsing next() manually:")
fib_gen = fibonacci(4)
print(next(fib_gen))  
print(next(fib_gen))  
print(next(fib_gen))  
print(next(fib_gen)) 