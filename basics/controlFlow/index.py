points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 25
guess = 30

if answer > guess:
    result = "Oops!  Your guess was too low."
elif answer < guess:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"

print(result)


# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA"
purchase_amount = 150

if state == "CA":
    tax_amount = 0.075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = 0.095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":
    tax_amount = 0.089
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit!"
elif points <= 150:
    prize = None
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.replace(" ", "_").lower())

print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for name in range(len(usernames)):
    usernames[name] = usernames[name].replace(" ", "_").lower()
print(usernames)


tokens = ["<greeting>", "Hello World!", "</greeting>"]
count = 0

# write your for loop here
for tag in tokens:
    print(tag)
    if tag.startswith("<") and tag.endswith(">"):
        count += 1

print(count)


items = ["first string", "second string"]
html_str = "<ul>\n"  # The "\n" here is the end-of-line char, causing
# chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)


# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {"apples": 4, "oranges": 19, "kites": 3, "sandwiches": 8}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Iterate through the dictionary
for key, value in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value
print(result)


# Example 1

result = 0
basket_items = {"pears": 5, "grapes": 19, "kites": 3, "sandwiches": 8, "bananas": 4}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Iterate through the dictionary
for key, value in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value

print(result)

# Example 2

result = 0
basket_items = {"peaches": 5, "lettuce": 2, "kites": 3, "sandwiches": 8, "pears": 4}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Iterate through the dictionary
for key, value in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value
print(result)


# Example 3

result = 0
basket_items = {"lettuce": 2, "kites": 3, "sandwiches": 8, "pears": 4, "bears": 10}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

# Iterate through the dictionary
for key, value in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value
print(result)


# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {"apples": 4, "oranges": 19, "kites": 3, "sandwiches": 8}
fruits = ["apples", "oranges", "pears", "peaches", "grapes", "bananas"]

for key, value in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        fruit_count += value
    # if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += value

print(fruit_count, not_fruit_count)

limit = 40

num = 0
while (num + 1) ** 2 < limit:
    num += 1
nearest_square = num ** 2

print(nearest_square)


headlines = [
    "Local Bear Eaten by Man",
    "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree",
    "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic",
]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for number in check_prime:
    if number % 2 == 0:
        print(
            "{} is NOT a prime number, because {} is a factor of {}".format(
                number, 2, number
            )
        )
    else:
        print("{} IS a prime number".format(number))


# Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends
# it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for (
    l,
    x,
    y,
    z,
) in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(l, x, y, z))
for point in points:
    print(point)


# Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}
for key, value in zip(cast_names, cast_heights):
    cast[key] = value
print(cast)


# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = [], []
names, heights = zip(*cast)


print(names)
print(heights)


# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height.
#  For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = [
    "Barney Stinson",
    "Robin Scherbatsky",
    "Ted Mosby",
    "Lily Aldrin",
    "Marshall Eriksen",
]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, height in enumerate(heights):
    cast[i] += " " + str(height)

print(cast)


# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower() for name in names]
print(first_names)


# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [i * 3 for i in range(1, 21)]
print(len(multiples_3))
print(multiples_3)



# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98,
}

passed = [name for name, value in scores.items() if value > 65]
print(passed)
