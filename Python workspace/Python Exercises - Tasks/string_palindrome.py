input_str = input("Enter a string:")
rev_str = input_str[::-1]
if(input_str == rev_str):
    print(f'{input_str} is a palindrome')
else:
    print(f'{input_str} is not a palindrome')