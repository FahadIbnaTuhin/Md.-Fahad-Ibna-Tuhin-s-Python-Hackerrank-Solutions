def capit(na):
    word_list = na.split(" ")
    for word in word_list:
        if word[0].isalpha():
            print(word[0].upper(), end="")
        else:
            print(word[0], end="")
        print(word[1:] + " ", end="")


name = "fahad 2abc tuhin"

capit(name)
