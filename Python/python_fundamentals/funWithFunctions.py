
def oddEven():
    for i in range(2001):
        if i%2 != 0:
            print("Number is {}. This is an odd number.".format(i))
        else:
            print("Number is {}. This is an even number.".format(i)) 

# oddEven()

def multiply(arr, val):
    for i in range(len(arr)):
        arr[i] *= val

    return arr


a = [2,4,3]

b = multiply(a, 2)



def layered_multiples(multi):
    twoD = []
    for i in range(len(multi)):
        print (twoD)
        twoDe = []
        for i in range(multi[i]):
            # print(multi[i])
            twoDe.append("1")
        twoD.append(twoDe)
        print (len(twoDe))

    return print(twoD)

layered_multiples(multiply([2, 3, 4], 2))