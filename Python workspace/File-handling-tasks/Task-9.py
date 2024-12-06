try:
    with open('sample_img.png', 'rb') as binaryFile:
        data = binaryFile.read()
        with open('copy_image.png', 'wb') as copyFile:
            copyFile.write(data)
except IOError:
    print("Some error occured")