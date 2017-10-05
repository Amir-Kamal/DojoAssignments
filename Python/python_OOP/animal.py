class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("{}'s health: {}".format(self.name, self.health))
        return self


yorkie = Animal("Fido")
yorkie.walk()
yorkie.walk()
yorkie.walk()
yorkie.run()
yorkie.run()
yorkie.display_health()

class Dog(Animal):
    def __init__(self, name):
        print("initiating dog...")
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5


dmx = Dog("DMX")

dmx.walk().walk().walk()
dmx.run().run()
dmx.pet()
dmx.display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display_health(self):
        super(Animal, self).display_health()
        print("I am a Dragon")
        return self


    
