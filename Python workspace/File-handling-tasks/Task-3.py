import os
try:
    a='sample.txt'
    if(os.path.exists(a)):
        print(f'{a} exists')
        with open('sample.txt', 'a') as file:
            file.write("Some new data by append mode.")
        with open('sample.txt', 'r') as file:
            print(file.read())
    else:
        print(f'{a} does not exists')
except FileNotFoundError:
    print("Error: File not present.")
except IOError:
    print("Error: Something went wrong.")