import random

class Person:
    def __init__(self, firstName, lastName, health, status):
        self.firstName = firstName
        self.lastName = lastName
        self.health = health
        self.status = status


    def introduce(self):
        print("Hello, my name is {} {}".format(self.firstName, self.lastName))


    def emotion(self):
        emo = random.randrange(1, 3)
        if emo == 1:
            print("{} is happy today".format(self.firstName))
        elif emo == 2:
            print("{} is said today".format(self.firstName))


    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstName))
        elif self.health >= 76:
            print("{} is little tired today".format(self.firstName))
        elif self.health >= 51:
            print("{} is feeling unwell".format(self.firstName))
        elif self.health >= 50:
            print("{} goes to a doctor".format(self.firstName))
        else:
            print("{} is unconscious".format(self.firstName))

Dheeraj = Person("Dheeraj", "Kumar Jha", 95, True)
Jaya = Person("Jaya", "Mishra", 88, False)
Mohit = Person("Mohit", "Jha", 72, True)

print("{} is my friend? {}".format(Dheeraj.firstName, Dheeraj.status))
print("{} is my friend? {}".format(Jaya.firstName, Jaya.status))
print("{} is my friend? {}".format(Mohit.firstName, Mohit.status))

Dheeraj.introduce()
Jaya.introduce()
Mohit.introduce()

Dheeraj.status_change()
Jaya.status_change()
Mohit.status_change()

Dheeraj.emotion()

# Here Enemy class is inheriting from Person class and
# should be able to use all the variables and methods from the Person's class
class Enemy(Person):
    def __init__(self, weapon, firstName, lastName, health, status):
        super().__init__(firstName, lastName, health, status)
        self.weapon = weapon

    def introduce(self):
        print("I am the enemy!!!")

    # self allows access to enemmy and other allows access to other person
    def hurt(self, other):
        if self.weapon == "rock":
            other.health = other.health - 10
        elif self.weapon == "stick":
            other.health = other.health - 5
        print(other.health)


    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstName))


    def steal(self, other):
        print("Ha ha ha, {}, I have your stuff".format(other.firstName))
        if other.status == True:
            other.status = False


Alex = Enemy("rock", "Alex", "Mahone", 75, False)
Alex.hurt(Dheeraj)
Alex.insult(Mohit)
Alex.steal(Jaya)

Alex.emotion()
Alex.status_change()

Alex.introduce()
