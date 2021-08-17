# Lesson Summary

Here's a recap of the data structures we covered.

## Data Structure

| Data Structure  | Ordered   |      Mutable       |  Constructor     | Example
| :-------------: | :-----:   | :----------------: |  :----------:    | :-----:
|   List          |    Yes    |         5          |  [ ] or list( )  | [5.7, 4, 'yes', 5.7]
|   Tuple         |   Yes     |        6.5         |  ( ) or tuple( ) | (5.7, 4, 'yes', 5.7)
|   Set           | NO        | "this is a string" |  { }* or set( )  | {5.7, 4, 'yes'}
|   Dictionary    |   NO      |   true or false    |  { } or dict( )  | {'Jun': 75, 'Jul': 89}


*You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().
** A dictionary itself is mutable, but each of its individual keys must be immutable.