# There can be one or multiple classes per file
# Multiple classes can be grouped based on commanality (similiar functionality)
# in one file

# inheritance - child/derived class can use attributes/methods of parent class
# multiple inheritance - child/derived class can inherit attributes/methods from multiple classes
# polymorphism - child/derived class can overide class methods of parent class

# __init__ method - allows every instance of the class to be created with specific parameters
"""
Sets the attributes for an object at object creation. It is a Constructor
It is not required but is generally used to set default state of object when it is created
It is always the first method for a class
"""
# self - allows information to be shared easily and efficiently

import random

class Person:
    def __init__(self, firstName, lastName, health, status):
        """
        initializes attributes to be used in/available for all
        class method in this class and for class objects created
        by this class.

        :param firstName:
        :param lastName:
        :param health:
        :param status:
        """
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

