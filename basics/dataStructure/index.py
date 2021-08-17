month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month - 1]
print(num_days)


eclipse_dates = [
    "June 21, 2001",
    "December 4, 2002",
    "November 23, 2003",
    "March 29, 2006",
    "August 1, 2008",
    "July 22, 2009",
    "July 11, 2010",
    "November 13, 2012",
    "March 20, 2015",
    "March 9, 2016",
]


# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.
population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0,"Mumbai":12.5}

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
print(population)