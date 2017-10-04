

class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print("Bike Info:")
        print("Price: {}".format(self.price))
        print("Maximum Speed: {}".format(self.max_speed))
        print("Miles: {}".format(self.miles))
        return self 

    def ride(self):
        print ("Riding.....")
        self.miles += 10
        print("Miles: {}".format(self.miles))
        return self 

    def reverse(self):
        print("Reversing.....")
        if self.miles > 0: self.miles -= 5
        print("Miles: {}".format(self.miles))
        return self

slic1 = Bike(850, 80)

print("="*30+"\n")
print(slic1.displayInfo())
print("="*30+"\n")
print(slic1.ride())
print("="*30+"\n")
print(slic1.ride())
print("="*30+"\n")
print(slic1.ride())
print("="*30+"\n")
print(slic1.reverse())
print("="*30+"\n")
print(slic1.displayInfo())
print("="*30+"\n")
print(slic1.reverse())
print("="*30+"\n")

slic2 = Bike(730, 70)

print(slic2.ride())
print("="*30+"\n")
print(slic2.ride())
print("="*30+"\n")
print(slic2.reverse())
print("="*30+"\n")
print(slic2.reverse())
print("="*30+"\n")
print(slic2.displayInfo())
print("="*30+"\n")


slic3 = Bike(950, 130)

print(slic3.reverse())
print("="*30+"\n")
print(slic3.reverse())
print("="*30+"\n")
print(slic3.reverse())
print("="*30+"\n")
print(slic3.displayInfo())
print("="*30+"\n")



    