





def stars(lst):
    for i in lst:
        try:
            print ("*"*int(i))
        except ValueError:
            print (i[0]*len(i))


y = [4, 6, 1, 3, 5, 7, 25]

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


stars(x)