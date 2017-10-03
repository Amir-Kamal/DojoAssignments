 

def typeList(list):
    newstr = ""
    sumi = 0.0
    for i in list:
        if type(i) == str:
            newstr += i
        elif type(i) == int or float:
            sumi += float(i)
    return print("String: {} Sum: {}".format(newstr, sumi)) 



zrx = ['magical unicorns',19,'hello',98.98,'world']

typeList(zrx)