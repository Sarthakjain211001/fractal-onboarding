num = int(input("Enter number: "))
x = num
fact = 1
while num>1:
    fact = fact*num
    num = num-1
print(f'Factorial of {x}: {fact}')