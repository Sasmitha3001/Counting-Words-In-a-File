def countWordsFromFile():
    file=input("Enter a file name\t")
    numOfWords=0
    fileDetails=open(file,'r')

    for i in fileDetails:
        words=i.split()
        print(words)
        numOfWords+=len(words)
    print("Number of words in the file are: ",numOfWords)

countWordsFromFile()

