name = input("Please enter your name. ")
if name == "Dheeraj":
    print("Hello {}!".format(name))
print("How are you doing?")

# elif
name_new = input("Please enter another name. ")
if name_new == "Dheeraj":
    print("Hello {}! Nice to see you.".format(name_new))
elif name_new == "Jaya":
    print("Hi {}! You look lovely today.".format(name_new))
elif name_new == "Mohit":
    print("Hey {}! You are a genius.".format(name_new))
print("Nothing matches.")