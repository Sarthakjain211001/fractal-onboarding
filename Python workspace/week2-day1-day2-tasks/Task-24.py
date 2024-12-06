fileF1 = open('sample_file.txt', 'r')
print(fileF1.read())

fileF1 = open('sample_file.txt', 'a')
fileF1.write("Some more text appended.")
fileF1.close()

fileF1 = open('sample_file.txt', 'r')
print(fileF1.read())

fileF2 = open("sample_file2.txt",'r')
