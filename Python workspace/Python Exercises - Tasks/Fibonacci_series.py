num = int(input("Enter number: "))
x = num-2
fibonacci_list=[0, 1]
i=0
while(x > 0):
    fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])
    i=i+1
    x=x-1
if(num == 1):
    print([0])
else:
    print(fibonacci_list)
