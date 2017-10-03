
myself = {"name": "Victor A.", "age":"27", "country of birth": "The United States", 
          "favorite language": "Python"}

def printMyself(dict):
    for key, val in dict.items():
        print ("My {} is {}".format(key, val))


printMyself(myself)