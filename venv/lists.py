fruits = ["peach", "pear", "apple"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

# .append() method - To add an item at the end of the list
fruits.append("orange")
print(fruits)

# .extend() method - To add one list to another
fruits.extend(years)
print(fruits)

# .remove() - Exact item name must be provided
fruits.remove("peach")
print(fruits)

# .pop() - Remove and return that item. Index based
removed_item = fruits.pop(0)
print(removed_item)
print(fruits)

# .pop() - If you are not sure the last index of the list
fruits.pop(-1)
print(fruits)

# .sort() - T sort lists having only same type of items
num = [1, 1.77, 311, 0, 0.88, -11, 444322, 22]
num.sort()
print(num)

# Check membership - Check if the item is there in the list or not
print(311 in num)
print("orange" in fruits)
print("Orange" in fruits)
