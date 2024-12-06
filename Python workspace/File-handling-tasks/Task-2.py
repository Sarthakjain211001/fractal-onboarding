try:
    #creating a file named report.txt and writing in it.
    with open('report.txt', 'w') as file:
        file.write('This is a new file named report.\nWriting some text in it.')
    #reading the file created previously
    with open('report.txt', 'r') as file:
        text = file.readlines()
        for line in text:
            words = line.split()
            print(words)
        # print(text)
except IOError:
    print("some error occured")