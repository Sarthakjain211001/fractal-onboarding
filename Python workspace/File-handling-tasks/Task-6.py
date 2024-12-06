try:
    with open('missing-file.txt','r') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Some error occured")    