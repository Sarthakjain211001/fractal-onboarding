try:
    text =""
    with open('sample.txt','r') as file:
        text = file.read()
    with open('destination.txt','w') as file:
        file.write(text)
except IOError:
    print("Some error occured")    