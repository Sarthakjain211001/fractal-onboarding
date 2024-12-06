try:
    newText =""
    original_word="text"
    new_word = "content"
    with open('sample.txt','r') as file:
        text = file.read()
        print("original content: ", text)
        newText = text.replace(original_word, new_word)
    with open('sample.txt','w') as file:
        file.write(newText)
    with open('sample.txt','r') as file:
        text = file.read()
        print("new content: ", text)
except IOError:
    print("Some error occured")    