try:
    #creating a file named sample.txt and writing in it.
    with open('sample.txt', 'w') as file:
        file.write('This is sample file. \nWriting some text in it.')
    #reading the file created previously
    with open('sample.txt', 'r') as file:
        text = file.read()
        print(text)
except IOError:
    print("some error occured")