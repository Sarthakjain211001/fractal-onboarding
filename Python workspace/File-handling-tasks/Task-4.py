try:
    count = 0
    with open('large_file.txt', 'r') as file:
        for line in file:
            print(line)
            count += 1
    print('number of lines: ',count)
except IOError:
    print("Some error occured")