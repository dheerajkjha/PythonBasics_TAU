def addition():
    num_one = 50
    num_two = 4
    print(num_one + num_two)

addition()

def user_info(name, age, city):
    print("{} is {} years old and lives in {}".format(name, age, city))

user_info("Sameer", 33, "Agra")

"""
Error messaage will be displayed as function has only two arguments
TypeError: user_info() missing 1 required positional argument: 'city'
"""
# user_info(32, "Melboure")

"""
Keyword aregument - We use it to define the default value of the argument
if the value is not passed as an argument in the function.
"""
def user_info_new(name, age = 0, city = "Tuscon"):
    print("{} is {} years old and lives in {}".format(name, age, city))


user_info_new("Raja")

# Through Keyword argument, we also need not to follow the sequence while passing the argument
user_info_new(age = 15, name = "Sachin", city = "London")


"""
*args - 
contents: allows for unlimited variables to be passed 
into a function without defining them during function definition
def add(*args):
print(sum(args))

add(2, 3, 4)
add(2, 4, 6, 8, 185)
"""

"""
*args - 
contents: allows for unlimited keyword arguments to be passed 
into a function without defining them during function definition
def application(**kwargs):
print(**kwargs)

application(name = "Jess", email = "mail@mail.com")
application(name = "Susan", surname = "Wright", age = 42)
"""


"""
Combining arg types - All three types can be used in a singles function.
They must be used in order : formal positional arguments, *args and **kwargs
"""
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}. ${} is her salary. She is {} years old.".format(fname, lname, company, email, *args))


application("Maria", "Smith", "mail@mail.com", "Teachcode.org", 7500, 55,  hire_date = "September 2010")
