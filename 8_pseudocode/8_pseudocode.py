Keyword	Meaning
START	start of the program
SET	set a variable that we can use for later
GET	retrieve input from user
PRINT	display output to user
READ	retrieve a value from a variable
IF/ELSE IF/ELSE	show conditional branches in logic
WHILE	show looping logic
END	end of the program

For example, write out pseudocode (both casual and formal) that does the following:

1. a function that returns the sum of two numbers
define a function which takes two arguments
return the addition of those two arguments.  
make sure that the arguments are turned into integers

START
# a function that returns the sum of two numbers
SET function (number1, number2)
    RETURN number1 + number2

END

a function that takes a list of strings, and returns a string that is all 
those strings concatenated together
you're giving a list in which all the elements are strings
you set an empty string
then you append each element of the list to the empty string
then you return that string

START
# a function that takes a list of strings, and returns a string that is all 
# those strings concatenated together

SET empty_string
LOOP through all the elements of a list
    APPEND element to the empty_string
RETURN empty_string


# a function that takes a list of integers, and returns a new list with every 
# other element from the original list, starting with the first element. 
# For instance: every_other([1,4,7,2,5]) # => [1,7,5]
Initialize a function which takes a list of integers as it's argument
Inialize a new empty list
Loop through the list for every other element, start with the first index.
Add the elements to empty list
Return the empty list

START

# Given a list of integers called "numbers"
# Return a new list with every other element, starting with the first

SET result = empty list
SET index = 0

WHILE index < length of numbers
    SET element = value in numbers at position index
    SET result = result + element  # add element to result list
    SET index = index + 2

RETURN result

END


# a function that determines the index of the 3rd occurrence of a given 
# character in a string. For instance, if the given character is 'x' and 
# the string is 'axbxcdxex', the function should return 6 (the index of the 
# 3rd 'x'). If the given character does not occur at least 3 times, return None.

initialize a function which takes a string and a character
initialize a integer variable which will count how many times the character
shows up in the string.  This should be set to zero initially.
loop through the string one character at a time, starting at the first character
if the character at the current index equals the character which was passed into 
the function, then the counting variable should go up by one.
within the loop, if the counting variable equals three, then return the current index

START

# Given a string called "text" and a character called "target"
# Return the index of the 3rd occurrence of target in text
# If target does not occur at least 3 times, return None

SET count = 0
SET index = 0

WHILE index < length of text
    IF text[index] == target
        SET count = count + 1
        IF count == 3
            RETURN index
    SET index = index + 1

RETURN None

END

a function that takes two lists of numbers and returns the result of merging 
the lists. The elements of the first list should become the elements at the 
even indexes of the returned list, while the elements of the second list 
should become the elements at the odd indexes. For instance:
Copy Code
merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

initialize a function which takes two lists. we must assume that both lists are the same length
initialize an index to zero.  this will iterate through both lists at the same time
initialize an empty list which will become the returned list
initialize a while loop which will loop until it gets to the length of one of the lists
add the current element of the first list to the empty list
add the current element of the second list to the empty list
after looping is over when the loop gets to the end of one of the lists, 
return the empty list which is now not empty

START

# Given two lists of numbers: list1 and list2
# Both lists have the same length
# Return a new list where:
#   - elements from list1 are at even indexes
#   - elements from list2 are at odd indexes

SET index = 0
SET result = empty list

WHILE index < length of list1
    SET result = result + list1[index]
    SET result = result + list2[index]
    SET index = index + 1

RETURN result

END