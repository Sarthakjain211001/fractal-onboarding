try:
    #reading from an existing file
    with open('data1.txt', 'r') as file1:
        txt = file1.read()
        print('file1 text:')
        print (txt)
    #writing to new file
    with open('data2.txt', 'w') as file2:
        file2.write(txt)
    #reading from new fil
    with open('data2.txt', 'r') as f2:
        txt2 = f2.read()
        print('file2 text:')
        print (txt2)
except FileNotFoundError:
    print("Error: FIle not found")
except IOError:
    print("Some error occured in file handling")