#square of each number form 1 to 10 using list comprehension
new_list = [item**2 for item in range(1,11)]
print(new_list)

#filtering out odd numbers. keeping only even numbers
new_list2 = [item for item in range(1,11) if item%2==0]
print(new_list2)