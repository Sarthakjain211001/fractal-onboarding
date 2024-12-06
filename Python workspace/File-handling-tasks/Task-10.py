try:
    with open('notes.txt','r') as file:
        text = file.read()
        print(text)
except IOError:
    print("Some error occured")  