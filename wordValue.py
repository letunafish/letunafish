while True:
    word = ""
    sum =0
    word = input("Enter a word: ")
    for i in word:
        #print(ord(i))
        sum += ord(i)
    print(sum)