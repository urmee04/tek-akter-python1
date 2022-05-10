# Comments are lines in a program that the program ignores when it executes. They allow you to add notes about how the program works to help you and other developers understand the code.

# This is a single line comment in Python

'''
Use comments to explain:
    • The role of important variables when you introduce them
    • How you’ve approached a problem after considering multiple approaches
    • What your functions do
    • What classes are used for in the program
    
    Writing comments will remind you what your code does when you return to it later. Comments also help teams of programmers collaborate effectively.
'''

'''
    This is a multi-line 
    comment in Python
'''

# Print to console
from array import array
from operator import le


print("This is my first print statement")

'''
In statically typed languages, you must declare the kind of data a variable represents when you define it. Python is a dynamically typed language, meaning you don’t have to declare the kind of data a variable will represent. In Python, the interpreter examines the data associated with the vari-able throughout the life of the program and manages type issues for you.
'''

'''
In Python, a variable is a name attached to a piece of data. You first define a variable, then use that name when you refer to that piece of data.
'''

# Initialize two string variables

first_name = "John"
last_name = "Doe"

'''
A string is a value made up of text and is one of the simplest data types in any language. Much of the information that’s passed within and between programs is strings.
Strings are treated as a collection of characters, so the string "123" is different from the numerical value 123. A substring is part of a string.
You can perform many actions with strings:
• Joining strings together, known as concatenation
• Inserting the value of a variable into a string, known as interpolation• Changing a string’s case
• Stripping extra whitespace from a string• Searching for a substring within a string
• Replacing some characters in a string
In Python, strings are enclosed using single or double quotes.
'''

# Concatenate strings
print("Hi, my name is " + first_name + " " + last_name)

# use % operator to concatenate
print("Hi, my name is %s %s" % (first_name, last_name))

# using join() to concatenate
print("Hi, my name is " + " ".join([first_name, last_name]))

# using format() to concatenate
print("Hi, my name is {} {}".format(first_name, last_name))

#TODO: Try introducing yourself and add your age as well. On top of first_name & last_name variable add another variable called my_age and set it to a number. 
# Then try concatenating it using the above four strategies.  

my_age = 30
first_name = "Romana"
last_name = "Akter"
# Concatenate strings
print("Hi, my name is " + first_name + " " + last_name + " and I am " + str(my_age) + " years old.")

# use % operator to concatenate
print("Hi, my name is %s %s and I am %d years old." % (first_name, last_name, my_age))

# using join() to concatenate
print(" ".join(["Hi, my name is", first_name, last_name,"and I am", str(my_age), "years old."])) 

# using format() to concatenate
print("Hi, my name is {} {} and I am {} years old." .format(first_name, last_name, my_age))


print("-------------------------------------------------------------------------------\n")

'''
Integers and floats are the two main kinds of numerical data types. An integer, or int, is a number with no decimal part. A float is a number with a decimal part.
'''

'''
You can perform all basic arithmetic operations with numerical data and do higher-order operations, such as working with exponents, finding absolute values, and work-ing with trigonometric functions.
Python allows you to represent complex numbers (numbers with real and imaginary parts) and work with fractions.
For computation-intensive work, third-party libraries, such as NumPy, SciPy, and pandas, can make your work easier. Many dedicated visualization libraries are available as well, such as Matplotlib, Bokeh, Pygal, and Plotly.
'''

# Initialize variables of different data types
simple_string  = "this is a simple string"
num            = 1234
simple_decimal = 12.4
simple_boolean = True #A Boolean value represents either true or false. In Python, these values are written as True and False.
short_array    = [1, 2, 3, 4]

'''
You can use the elif, or else if, statement to make your program respond to multiple conditions. This code structure means “if one condition applies, do this; else if a different condition applies, do something different.” You can chain together as many of these specific conditions as you need.
An else block runs a particular block of code when all other conditions don’t apply. An else block must always be the last block in an if-elif-else chain.
'''
# Branching Logic
if(simple_decimal < 5.0):
    print("Small decimal")
elif(simple_decimal < 9.0):
    print("Mid size decimal")
else:
    print("Big decimal") 

'''
A sequence is a data structure that stores a collection of items in a specific order. In some languages, a sequence can only contain items of one type; in other languages, including Python, a sequence can have items of different types.
'''
print('--------- printing array from the first index -----------------\n')

# Control flow - for loops
for num in short_array:
    print(num)

print("------- printing array from the last index -----------\n")

'''
A loop is a block of code that runs multiple times. Use loops when you need to repeat actions more than once, depending on certain criteria. The two loop types are the for loop and the while loop.
'''
# loop through an array from the last index
for index in range(len(short_array) - 1, -1, -1):
    print(short_array[index])

print("----- Print Odd Numbers ---------------------\n")

'''
A for loop repeats as many times as you specify or once for each item in a sequence. For example, you can write a for loop that runs 100 times to repeat an action 100 times. You can also write a for loop that runs once for each item in a collection of items.
'''
# for loops print odd numbers from 1 - 10;
for num in range(10):
    if(num % 2 == 1):
        print(num)

# or ...

for num in range(10):
    if(num % 2 != 0):
        print(num)

print("----------- While Loop -------------------\n")

'''
A while loop runs as long as a certain condition is true. Say you have a game loop that runs as long as a game_active variable is set to True. You can then put mul-tiple situations inside the loop that cause game_active to become False and end the game. You can also use a while loop to process items in a collection that might have new items added to it as the loop is running. As long as items are in the collection, you can keep working with it. When the collection is empty, the loop stops running.
'''
# While Loop
while_loop_index = 1
while while_loop_index < 10:
    print(while_loop_index)
    while_loop_index += 1;    

'''
A nested loop is a loop inside another loop. Say you need a loop that examines every pixel in an image. You could write a loop that looks at each pixel in a row and, inside that loop, add a second loop that looks at every pixel in the current column for that row.
'''
#TODO: write a for loop to ONLY print even numbers
start = int(input("Enter start of a number range: "))
end = int(input("Enter end of a number range: "))

for num in range(start, end + 1):
    if num % 2 == 0:
       print(num, end = " ")



#TODO: Declare an Array with mixed data types. i.e. string, number, boolean, etc. 
# Iterate through this list using for loop and see the output. 

elements = ["Romana", 2, 2.02, True, 1j, ["grape","apple"], range(2), {"name" : "Romana", "age" : 50}, {"apple", "banana", "cherry"}, b"Hello", bytearray(5), memoryview(bytes(5)), frozenset({"apple", "banana", "cherry"}), None ]
for elem in elements:
    print(elem)


#TODO: Print the data type for each array item. 

elements = ["Romana", 2, 2.02, True, 1j, ["grape","apple"], range(2), {"name" : "Romana", "age" : 50}, {"apple", "banana", "cherry"}, b"Hello", bytearray(5), memoryview(bytes(5)), frozenset({"apple", "banana", "cherry"}), None ]
for elem in elements:
    print(type(elem))


# TODO: Reverse a String: input = hello, output = olleh
a_str = input("Enter string: ")
reversed_str="".join(reversed(a_str)) 
print(reversed_str) 


# TODO: Reverse a number: input = 1234, output = 4321
num = int(input("Enter a number: "))
n_str = str(num)
reversed_num="".join(reversed(n_str)) 
print(reversed_num) 
        

'''
Sequences are important when you need to store items in a specific order. For example, a list of website users might be ordered according to when each user registered.
With a sequence, you can do the following:
• Add and remove items
• Work with individual items or groups of items
• Determine whether a value is in the sequence
• Look for duplicate or unique items
• Loop through the sequence and do something with each item
• Work with items that match certain conditions.
In Python, the main sequence type is the list. Lists are mutable, meaning you can modify them after creating them. Tuples are immutable sequences, meaning they can’t be changed after they’re defined. Strings are a special type of sequence: each element in the sequence is a character.
'''
print("------- List --------------")
my_list = ["apple", "banana", "cherry", "mango", "pineapple", "watermelon"]

# print the first item of a list
print(my_list[0])

# print the last item of a list
print(my_list[-1])

# print a range of items 
print(my_list[0:3])

# add item to the end of the list
my_list.append("Cupcake")
print(my_list)

# add item to a specified index
my_list.insert(1, "Chips")
print(my_list)

# remove an item off of a list
my_list.remove("Cupcake")
print(my_list)

# remove an item off of a list by index #
my_list.pop(-1) # last index removal
print(my_list)

# size of a list
print(len(my_list))

print("--------- Iterate through my_list---------------")
# iterate through a list using for loop
for fruit in my_list:
    print(fruit)

# update an item in the list by index 
my_list[1] = "avocado"

# Iterate through a list with access to index and item in the list using enumerate
for index, fruit in enumerate(my_list):
    print("index: %s =  %s " % (index, fruit))

#TODO: Using a for loop update every item in the my_list list into dessert items

dessert = ["apple cake", "banana cake", "donut", "fudge", "ice cream", "jilapi"]

 
for i in range(len(my_list)):
  
    # update every item in the my_list list into dessert items
   
    if my_list[i] == my_list[0]:
        my_list[i] = dessert[0]
  
    if my_list[i] == my_list[1]:
        my_list[i] =  dessert[1]
        
    if my_list[i] == my_list[2]:
         my_list[i] =  dessert[2]
         
    if my_list[i] == my_list[3]:
          my_list[i] =  dessert[3]
          
    if my_list[i] == my_list[4]:
         my_list[i] =  dessert[4]
         
    if my_list[i] == my_list[5]:
         my_list[i] =  dessert[5]
            
print(my_list)

           
print("-------------------- Dictionary ---------------------------------\n")
# initialize dictionary
# Empty dictionary initialization
empty_dict = {}
print("Empty dictionary: %s" % empty_dict)

# Initialize dictionary with some key/pair values
country_capital_dict = {"America": "Washington DC", "Bangladesh": "Dhaka", "Canada": "Ottawa", "Denmark": "Copenhagen", "Ethopia": "Addis Ababa"}
print("\nDictionary with initialized values:\n%s" % country_capital_dict)

# adding items to an existing dictionary
country_capital_dict["France"] = "Paris"
country_capital_dict["Germany"] = "Berlin"
print("\nDictionary with new item added:\n%s" % country_capital_dict)

# Removing items from an existing dictionary 
#NOTE: dict.pop() is preferable method of removing an item from a dictionary. Also, del can delete an entire dictionary when you don't specify key to delete. 
del country_capital_dict["Germany"]
country_capital_dict.pop("France")
print("\nDictionary after deletion:\n%s" % country_capital_dict)

# updating values in a dictionary
country_capital_dict["Bangladesh"] = "Sylhet"
print("\nDictionary after update:\n%s" % country_capital_dict)

# Accessing values in a dictionary
print("\nCapital of Canada is: %s" %country_capital_dict.get("Canada"))

print("Capital of Denmark is: %s" % country_capital_dict["Denmark"])

print("\n----------------------- Iterate through a Dictionary------------------------------\n")
# Using for-loops to iterate through a dictionary:
for key, value in country_capital_dict.items():
    print("Country: %s, Capital City: %s" % (key, value))

#TODO: Create 5 lists of real life items and create 5 dictionaries. For example, 
# for list, I would create a list for list of chores I need to do on weekends. i.e chores = ['laundry', 'pick-up mail', 'clean the apt']
sports = ["cricket", "football", "golf", "hockey"]
pastimes = ["watching movie", "playing games", "playing music", "gardening"]
grocery_items = ["rice", "oil", "milk", "eggs"]
vegetable_items = ["broccoli", "spinach", "tomato", "potato"]
gardening_tools = ["shovel", "hoe", "rake", "watering can"]

print(sports)
print(pastimes)
print(grocery_items)
print(vegetable_items)
print(gardening_tools)

# for dictionary, I would have friends to phone number. friends = {'jose': '718-233-6464', 'ali': '646-232-2323'}
myPrincess = {"Cinderella":"blue", "Belle":"yellow", "Rapunzel":"purple"}
monthlySpending = {"food":100, "rent":950, "electric":100}
myInventory = {"sprockets" : 5, "widgets" : 11, "cogs" : 3}
myPastimes = {"game": "badminton", "hobby": "gardening", "music": "rock"}
myFruits = {1: "orange", 2: "mango", 3: "jackfruit"}

print(myPrincess)
print(monthlySpending)
print(myInventory)
print(myPastimes)
print(myFruits)


