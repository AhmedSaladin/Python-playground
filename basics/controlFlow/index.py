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


# Question 1.
# A. Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.

# B. Provide a dictionary with the count of Oscar wins for each director in the winners list.

nominated = {
    1931: [
        "Norman Taurog",
        "Wesley Ruggles",
        "Clarence Brown",
        "Lewis Milestone",
        "Josef Von Sternberg",
    ],
    1932: ["Frank Borzage", "King Vidor", "Josef Von Sternberg"],
    1933: ["Frank Lloyd", "Frank Capra", "George Cukor"],
    1934: ["Frank Capra", "Victor Schertzinger", "W. S. Van Dyke"],
    1935: ["John Ford", "Michael Curtiz", "Henry Hathaway", "Frank Lloyd"],
    1936: [
        "Frank Capra",
        "William Wyler",
        "Robert Z. Leonard",
        "Gregory La Cava",
        "W. S. Van Dyke",
    ],
    1937: [
        "Leo McCarey",
        "Sidney Franklin",
        "William Dieterle",
        "Gregory La Cava",
        "William Wellman",
    ],
    1938: [
        "Frank Capra",
        "Michael Curtiz",
        "Norman Taurog",
        "King Vidor",
        "Michael Curtiz",
    ],
    1939: ["Sam Wood", "Frank Capra", "John Ford", "William Wyler", "Victor Fleming"],
    1940: [
        "John Ford",
        "Sam Wood",
        "William Wyler",
        "George Cukor",
        "Alfred Hitchcock",
    ],
    1941: [
        "John Ford",
        "Orson Welles",
        "Alexander Hall",
        "William Wyler",
        "Howard Hawks",
    ],
    1942: [
        "Sam Wood",
        "Mervyn LeRoy",
        "John Farrow",
        "Michael Curtiz",
        "William Wyler",
    ],
    1943: [
        "Michael Curtiz",
        "Ernst Lubitsch",
        "Clarence Brown",
        "George Stevens",
        "Henry King",
    ],
    1944: [
        "Leo McCarey",
        "Billy Wilder",
        "Otto Preminger",
        "Alfred Hitchcock",
        "Henry King",
    ],
    1945: [
        "Billy Wilder",
        "Leo McCarey",
        "Clarence Brown",
        "Jean Renoir",
        "Alfred Hitchcock",
    ],
    1946: [
        "David Lean",
        "Frank Capra",
        "Robert Siodmak",
        "Clarence Brown",
        "William Wyler",
    ],
    1947: [
        "Elia Kazan",
        "Henry Koster",
        "Edward Dmytryk",
        "George Cukor",
        "David Lean",
    ],
    1948: [
        "John Huston",
        "Laurence Olivier",
        "Jean Negulesco",
        "Fred Zinnemann",
        "Anatole Litvak",
    ],
    1949: [
        "Joseph L. Mankiewicz",
        "Robert Rossen",
        "William A. Wellman",
        "Carol Reed",
        "William Wyler",
    ],
    1950: [
        "Joseph L. Mankiewicz",
        "John Huston",
        "George Cukor",
        "Billy Wilder",
        "Carol Reed",
    ],
    1951: [
        "George Stevens",
        "John Huston",
        "Vincente Minnelli",
        "William Wyler",
        "Elia Kazan",
    ],
    1952: [
        "John Ford",
        "Joseph L. Mankiewicz",
        "Cecil B. DeMille",
        "Fred Zinnemann",
        "John Huston",
    ],
    1953: [
        "Fred Zinnemann",
        "Charles Walters",
        "William Wyler",
        "George Stevens",
        "Billy Wilder",
    ],
    1954: [
        "Elia Kazan",
        "George Seaton",
        "William Wellman",
        "Alfred Hitchcock",
        "Billy Wilder",
    ],
    1955: ["Delbert Mann", "John Sturges", "Elia Kazan", "Joshua Logan", "David Lean"],
    1956: [
        "George Stevens",
        "Michael Anderson",
        "William Wyler",
        "Walter Lang",
        "King Vidor",
    ],
    1957: ["David Lean", "Mark Robson", "Joshua Logan", "Sidney Lumet", "Billy Wilder"],
    1958: [
        "Richard Brooks",
        "Stanley Kramer",
        "Robert Wise",
        "Mark Robson",
        "Vincente Minnelli",
    ],
    1959: [
        "George Stevens",
        "Fred Zinnemann",
        "Jack Clayton",
        "Billy Wilder",
        "William Wyler",
    ],
    1960: [
        "Billy Wilder",
        "Jules Dassin",
        "Alfred Hitchcock",
        "Jack Cardiff",
        "Fred Zinnemann",
    ],
    1961: [
        "J. Lee Thompson",
        "Robert Rossen",
        "Stanley Kramer",
        "Federico Fellini",
        "Robert Wise",
        "Jerome Robbins",
    ],
    1962: [
        "David Lean",
        "Frank Perry",
        "Pietro Germi",
        "Arthur Penn",
        "Robert Mulligan",
    ],
    1963: [
        "Elia Kazan",
        "Otto Preminger",
        "Federico Fellini",
        "Martin Ritt",
        "Tony Richardson",
    ],
    1964: [
        "George Cukor",
        "Peter Glenville",
        "Stanley Kubrick",
        "Robert Stevenson",
        "Michael Cacoyannis",
    ],
    1965: [
        "William Wyler",
        "John Schlesinger",
        "David Lean",
        "Hiroshi Teshigahara",
        "Robert Wise",
    ],
    1966: [
        "Fred Zinnemann",
        "Michelangelo Antonioni",
        "Claude Lelouch",
        "Richard Brooks",
        "Mike Nichols",
    ],
    1967: [
        "Arthur Penn",
        "Stanley Kramer",
        "Richard Brooks",
        "Norman Jewison",
        "Mike Nichols",
    ],
    1968: [
        "Carol Reed",
        "Gillo Pontecorvo",
        "Anthony Harvey",
        "Franco Zeffirelli",
        "Stanley Kubrick",
    ],
    1969: [
        "John Schlesinger",
        "Arthur Penn",
        "George Roy Hill",
        "Sydney Pollack",
        "Costa-Gavras",
    ],
    1970: [
        "Franklin J. Schaffner",
        "Federico Fellini",
        "Arthur Hiller",
        "Robert Altman",
        "Ken Russell",
    ],
    1971: [
        "Stanley Kubrick",
        "Norman Jewison",
        "Peter Bogdanovich",
        "John Schlesinger",
        "William Friedkin",
    ],
    1972: [
        "Bob Fosse",
        "John Boorman",
        "Jan Troell",
        "Francis Ford Coppola",
        "Joseph L. Mankiewicz",
    ],
    1973: [
        "George Roy Hill",
        "George Lucas",
        "Ingmar Bergman",
        "William Friedkin",
        "Bernardo Bertolucci",
    ],
    1974: [
        "Francis Ford Coppola",
        "Roman Polanski",
        "Francois Truffaut",
        "Bob Fosse",
        "John Cassavetes",
    ],
    1975: [
        "Federico Fellini",
        "Stanley Kubrick",
        "Sidney Lumet",
        "Robert Altman",
        "Milos Forman",
    ],
    1976: [
        "Alan J. Pakula",
        "Ingmar Bergman",
        "Sidney Lumet",
        "Lina Wertmuller",
        "John G. Avildsen",
    ],
    1977: [
        "Steven Spielberg",
        "Fred Zinnemann",
        "George Lucas",
        "Herbert Ross",
        "Woody Allen",
    ],
    1978: [
        "Hal Ashby",
        "Warren Beatty",
        "Buck Henry",
        "Woody Allen",
        "Alan Parker",
        "Michael Cimino",
    ],
    1979: [
        "Bob Fosse",
        "Francis Coppola",
        "Peter Yates",
        "Edouard Molinaro",
        "Robert Benton",
    ],
    1980: [
        "David Lynch",
        "Martin Scorsese",
        "Richard Rush",
        "Roman Polanski",
        "Robert Redford",
    ],
    1981: [
        "Louis Malle",
        "Hugh Hudson",
        "Mark Rydell",
        "Steven Spielberg",
        "Warren Beatty",
    ],
    1982: [
        "Wolfgang Petersen",
        "Steven Spielberg",
        "Sydney Pollack",
        "Sidney Lumet",
        "Richard Attenborough",
    ],
    1983: [
        "Peter Yates",
        "Ingmar Bergman",
        "Mike Nichols",
        "Bruce Beresford",
        "James L. Brooks",
    ],
    1984: [
        "Woody Allen",
        "Roland Joffe",
        "David Lean",
        "Robert Benton",
        "Milos Forman",
    ],
    1985: [
        "Hector Babenco",
        "John Huston",
        "Akira Kurosawa",
        "Peter Weir",
        "Sydney Pollack",
    ],
    1986: ["David Lynch", "Woody Allen", "Roland Joffe", "James Ivory", "Oliver Stone"],
    1987: [
        "Bernardo Bertolucci",
        "Adrian Lyne",
        "John Boorman",
        "Norman Jewison",
        "Lasse Hallstrom",
    ],
    1988: [
        "Barry Levinson",
        "Charles Crichton",
        "Martin Scorsese",
        "Alan Parker",
        "Mike Nichols",
    ],
    1989: [
        "Woody Allen",
        "Peter Weir",
        "Kenneth Branagh",
        "Jim Sheridan",
        "Oliver Stone",
    ],
    1990: [
        "Francis Ford Coppola",
        "Martin Scorsese",
        "Stephen Frears",
        "Barbet Schroeder",
        "Kevin Costner",
    ],
    1991: [
        "John Singleton",
        "Barry Levinson",
        "Oliver Stone",
        "Ridley Scott",
        "Jonathan Demme",
    ],
    1992: [
        "Clint Eastwood",
        "Neil Jordan",
        "James Ivory",
        "Robert Altman",
        "Martin Brest",
    ],
    1993: [
        "Jim Sheridan",
        "Jane Campion",
        "James Ivory",
        "Robert Altman",
        "Steven Spielberg",
    ],
    1994: [
        "Woody Allen",
        "Quentin Tarantino",
        "Robert Redford",
        "Krzysztof Kieslowski",
        "Robert Zemeckis",
    ],
    1995: [
        "Chris Noonan",
        "Tim Robbins",
        "Mike Figgis",
        "Michael Radford",
        "Mel Gibson",
    ],
    1996: [
        "Anthony Minghella",
        "Joel Coen",
        "Milos Forman",
        "Mike Leigh",
        "Scott Hicks",
    ],
    1997: [
        "Peter Cattaneo",
        "Gus Van Sant",
        "Curtis Hanson",
        "Atom Egoyan",
        "James Cameron",
    ],
    1998: [
        "Roberto Benigni",
        "John Madden",
        "Terrence Malick",
        "Peter Weir",
        "Steven Spielberg",
    ],
    1999: [
        "Spike Jonze",
        "Lasse Hallstrom",
        "Michael Mann",
        "M. Night Shyamalan",
        "Sam Mendes",
    ],
    2000: [
        "Stephen Daldry",
        "Ang Lee",
        "Steven Soderbergh",
        "Ridley Scott",
        "Steven Soderbergh",
    ],
    2001: [
        "Ridley Scott",
        "Robert Altman",
        "Peter Jackson",
        "David Lynch",
        "Ron Howard",
    ],
    2002: [
        "Rob Marshall",
        "Martin Scorsese",
        "Stephen Daldry",
        "Pedro Almodovar",
        "Roman Polanski",
    ],
    2003: [
        "Fernando Meirelles",
        "Sofia Coppola",
        "Peter Weir",
        "Clint Eastwood",
        "Peter Jackson",
    ],
    2004: [
        "Martin Scorsese",
        "Taylor Hackford",
        "Alexander Payne",
        "Mike Leigh",
        "Clint Eastwood",
    ],
    2005: [
        "Ang Lee",
        "Bennett Miller",
        "Paul Haggis",
        "George Clooney",
        "Steven Spielberg",
    ],
    2006: [
        "Alejandro Gonzaalez Inarritu",
        "Clint Eastwood",
        "Stephen Frears",
        "Paul Greengrass",
        "Martin Scorsese",
    ],
    2007: [
        "Julian Schnabel",
        "Jason Reitman",
        "Tony Gilroy",
        "Paul Thomas Anderson",
        "Joel Coen",
        "Ethan Coen",
    ],
    2008: [
        "David Fincher",
        "Ron Howard",
        "Gus Van Sant",
        "Stephen Daldry",
        "Danny Boyle",
    ],
    2009: [
        "James Cameron",
        "Quentin Tarantino",
        "Lee Daniels",
        "Jason Reitman",
        "Kathryn Bigelow",
    ],
    2010: [
        "Darren Aronofsky",
        "David O. Russell",
        "David Fincher",
        "Ethan Coen",
        "Joel Coen",
        "Tom Hooper",
    ],
}
winners = {
    1931: ["Norman Taurog"],
    1932: ["Frank Borzage"],
    1933: ["Frank Lloyd"],
    1934: ["Frank Capra"],
    1935: ["John Ford"],
    1936: ["Frank Capra"],
    1937: ["Leo McCarey"],
    1938: ["Frank Capra"],
    1939: ["Victor Fleming"],
    1940: ["John Ford"],
    1941: ["John Ford"],
    1942: ["William Wyler"],
    1943: ["Michael Curtiz"],
    1944: ["Leo McCarey"],
    1945: ["Billy Wilder"],
    1946: ["William Wyler"],
    1947: ["Elia Kazan"],
    1948: ["John Huston"],
    1949: ["Joseph L. Mankiewicz"],
    1950: ["Joseph L. Mankiewicz"],
    1951: ["George Stevens"],
    1952: ["John Ford"],
    1953: ["Fred Zinnemann"],
    1954: ["Elia Kazan"],
    1955: ["Delbert Mann"],
    1956: ["George Stevens"],
    1957: ["David Lean"],
    1958: ["Vincente Minnelli"],
    1959: ["William Wyler"],
    1960: ["Billy Wilder"],
    1961: ["Jerome Robbins", "Robert Wise"],
    1962: ["David Lean"],
    1963: ["Tony Richardson"],
    1964: ["George Cukor"],
    1965: ["Robert Wise"],
    1966: ["Fred Zinnemann"],
    1967: ["Mike Nichols"],
    1968: ["Carol Reed"],
    1969: ["John Schlesinger"],
    1970: ["Franklin J. Schaffner"],
    1971: ["William Friedkin"],
    1972: ["Bob Fosse"],
    1973: ["George Roy Hill"],
    1974: ["Francis Ford Coppola"],
    1975: ["Milos Forman"],
    1976: ["John G. Avildsen"],
    1977: ["Woody Allen"],
    1978: ["Michael Cimino"],
    1979: ["Robert Benton"],
    1980: ["Robert Redford"],
    1981: ["Warren Beatty"],
    1982: ["Richard Attenborough"],
    1983: ["James L. Brooks"],
    1984: ["Milos Forman"],
    1985: ["Sydney Pollack"],
    1986: ["Oliver Stone"],
    1987: ["Bernardo Bertolucci"],
    1988: ["Barry Levinson"],
    1989: ["Oliver Stone"],
    1990: ["Kevin Costner"],
    1991: ["Jonathan Demme"],
    1992: ["Clint Eastwood"],
    1993: ["Steven Spielberg"],
    1994: ["Robert Zemeckis"],
    1995: ["Mel Gibson"],
    1996: ["Anthony Minghella"],
    1997: ["James Cameron"],
    1998: ["Steven Spielberg"],
    1999: ["Sam Mendes"],
    2000: ["Steven Soderbergh"],
    2001: ["Ron Howard"],
    2002: ["Roman Polanski"],
    2003: ["Peter Jackson"],
    2004: ["Clint Eastwood"],
    2005: ["Ang Lee"],
    2006: ["Martin Scorsese"],
    2007: ["Ethan Coen", "Joel Coen"],
    2008: ["Danny Boyle"],
    2009: ["Kathryn Bigelow"],
    2010: ["Tom Hooper"],
}

### Question 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}
# Add your solution code below before line 10. Add more lines for your code as needed.
for year, names in nominated.items():
    for name in names:
        if nom_count_dict.get(name):
            nom_count_dict[name] += 1
        else:
            nom_count_dict[name] = 1

print("nom_count_dict = {}\n".format(nom_count_dict))
###################################################################################################################
###################################################################################################################

### Question 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}
# Add your solution code below before line 20. Add more lines for your code as needed.
for year, names in winners.items():
    for name in names:
        if win_count_dict.get(name):
            win_count_dict[name] += 1
        else:
            win_count_dict[name] = 1


print("win_count_dict = {}".format(win_count_dict))
