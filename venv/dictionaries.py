# Initializing a dictionary
# Key Value pairs
stuff = {"food": 15, "energy": 100, "enemies": 3}

#. get() method - returns tha value of the key passed as an argument
print(stuff.get("energy"))

# .items() method - returns all the key value pairs of the dictionary in order
print(stuff.items())

# .keys() method - returns all the keys of the dictionary
print(stuff.keys())

# .popitem() - Removes the last key-value pair from the dictionary
stuff.popitem()
print(stuff)  # {'food': 15, 'energy': 100}

# .setdefault() method - Retrieves the value for a specific key
# or add a new key and default value into the dictionary
print(stuff.setdefault("food"))  # 15

# .setdefault() method - Also allows us to set a default value when
# the key is not in the dictionary
print(stuff.setdefault("friends", 1213))  # 1213
print(stuff)  # {'food': 15, 'energy': 100, 'friends': 1213}

# .update() method - updates the called dictionary
dic_one = {"Friends": 4, "Enemeies": 10,}
dic_two = {"rocks": 10, "arrows":22, "guns": 222}
dic_one.update(dic_two)
print(dic_one)  # {'Friends': 4, 'Enemeies': 10, 'rocks': 10, 'arrows': 22, 'guns': 222}
dic_one.update(dic_one)
print(dic_one)  # {'Friends': 4, 'Enemeies': 10, 'rocks': 10, 'arrows': 22, 'guns': 222}

dic_one.update(Friends = 44, Enemeies = 123)
print(dic_one)  # {'Friends': 44, 'Enemeies': 123, 'rocks': 10, 'arrows': 22, 'guns': 222}
dic_one.update(Bombs = 122)
print(dic_one)  # {'Friends': 44, 'Enemeies': 123, 'rocks': 10, 'arrows': 22, 'guns': 222, 'Bombs': 122}