with open("file.name", "r") as filename:
    filename = filename.read()





file = filename

fnep = file.rfind('.') #fnep stands for file name extension point
print(fnep)


if fnep != -1:
    fe=file[fnep+1:] #fe stands for file extension
    f = open("file.extension", "a")
    print(fe, file=f)
    f.close()
