def findChar(list, char):
    newList = []
    for i in list:
        if char in i:
            newList.append(i)
    return print(newList)



word_list = ['hello','world','my','name','is','Anna']
char = "a"

findChar(word_list, char)