

def number_input():

    user_input = input("Give me a number! : ")
    if int(user_input) < 100:
        return print("That's a small number")
    elif int(user_input) >= 100:
        return print("That's a big number!")



def string_size():
 
    user_input = input("Give me a sentence! : ")
    if len(user_input) >= 50:
        return print ("Long sentence")
    else:
        return print ("Short sentence")


# string_size()

def list_size():
 
    user_input = list(input("Give me a list! : "))
    if len(user_input) >= 10:
        return print ("Long list")
    else:
        return print ("Short list")

list_size()
