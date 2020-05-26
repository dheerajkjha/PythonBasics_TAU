fruits = ["Apple", "Melon", "Cherry", "Banana", "Pear"]

for fruit in fruits:
    print("Would you like to have {}.".format(fruit))

# For loop - Stepped 1 by default
for number in range(1, 11):
    print("Number : {} ".format(number))

# For loop - Stepped 2 by default
for number in range(1, 11, 2):
    print("Number : {} ".format(number))

# For loop - Stepped -3 by default
for number in range(13, 1, -3):
    print("Number : {} ".format(number))



# while loop
temp_far = 40
while temp_far > 32:
    print("Temprature of water is {}.".format(temp_far))
    temp_far -= 1
print("Water is now frozen and temp is {}.".format(temp_far))


# Loop Controls
# break - End the loop, go to the next statement in the program (Outside the loop)
temp_far = 40
while temp_far > 32:
    print("Temprature of water is {}.".format(temp_far))
    temp_far -= 1
    if temp_far == 33:
        break
print("Water is now frozen and temp is {}.".format(temp_far))


# continue - Skips current part of the loop and moved to the next part
for number_new in range(1, 10):
    if number_new == 6:
        print("We are skipping {}". format(number_new))
        continue
    print("Number : {}".format(number_new))


# pass - Skips any part of the loop where pass appears. Best used for test code
for num_new in range(1, 10):
    if num_new == 3:
        pass
    else:
        print("Number is : {}".format(num_new))
