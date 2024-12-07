list_ls = []
n = int(input("Enter n: "))
commands = ['insert', 'append', 'remove', 'pop', 'sort', 'reverse', 'print']

while n>0:
    cmd = input("Enter the command:")
    if(cmd == commands[0]):
        num = int(input("Enter number: "))
        idx = int(input("Enter position: "))
        list_ls.insert(idx, num)
    elif(cmd == commands[1]):
        num = int(input("Enter number: "))
        list_ls.append(num)
    elif(cmd == commands[2]):
        num = int(input("Enter number to be removed: "))
        list_ls.remove(num)
    elif(cmd == commands[3]):
        num = int(input("Enter number: "))
        list_ls.pop()
    elif(cmd == commands[4]):
        list_ls.sort()
    elif(cmd == commands[5]):
        rev_ls = list_ls[::-1]
        list_ls = rev_ls
    elif(cmd == commands[6]):
        print(list_ls)
    else:   #If no such comand
        print("No such command")
    