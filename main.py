"""Python for Visual Effects.

Assignment #2 - Functions and Conditionals
Answer the following questions.

Remember to be precise with the answer. The code will be tested using a pytest 
which will compare strings and values.
You need to type things exactly as they are or you will get a syntax error.
"Hello" == "hello"
>> false

Test your code before commiting and pushing to Github, be sure it
works as expected. Later, remove any code used to test the functions from this 
file and then commit and push.

"""
# 1.- Complete the body of the format_name function. 
# This function receives first_name and last_name, then prints a formatted 
# string of "Name: last_name, first_name" if both names are not blank, or 
# "Name: <first_name or last_name>" with just one of the names, if the other one
# is blank, and nothing if both are blank.
# Add the docstring in the function.
def format_name(first_name, last_name):
    # code goes here
    return ""
def format_name(first_name, last_name):
    if first_name != "" and last_name != "":
        return f"Name: {last_name}, {first_name}"
    elif first_name != "":
        return f"Name: {first_name}"
    elif last_name != "":
        return f"Name: {last_name}"
    else:
        return ""    


# 2.- Flesh out the body of the get_seconds function so that it RETURNS the
# total amount of seconds given the hours, minutes and seconds function
# arguments. Remember that there are 3600 seconds in an hour and 60 seconds in
# a minute. Must return an integer.
# Add the docstring in the function.
def get_seconds(hours, minutes, seconds):
    # code goes here
    return
def get_seconds(hours, minutes, seconds):
    return ((hours*3600) + (minutes*60) + seconds)

# 3.- Complete the function by filling in the missing parts. 
# The color_translator function receives the name of a color, then prints its 
# hexadecimal value. Currently, it only supports the three additive primary 
# colors (red, green, blue), so it returns "unknown" for all other colors.
# Add the docstring in the function.
# IMPORTANT: Delete the underscores.

def color_translator(color):
    if color.lower() == "red":
        hex_color = "#ff0000"
    elif color.lower() == "green":
        hex_color = "#00ff00"
    elif color.lower() == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

# 4.- In this scenerio, we have a directory with 5 files in it. Each file has a
# a different size: 2048, 4357, 97658, 125 and 8. calculate the average file
# file size by having Python add all the values for you, and then set the amount 
# variable to the amount of files. Finally, RETURN a message saying:
# "The average size is: X" followed by the resulting number. Remember to use the
# str() function to convert the number into a string.
# Use those values directly inside the function, no need to add them as
# arguments.
# Add the docstring in the function.
def average_size():
    # code goes here
    return ""
def average_size():
    amount = 5
    average_file_size = (2048+4357+97658+125+8)/amount
    return f"The average size is: {average_file_size}"

# 5.- Complete the following function. It must convert from Celsius to 
# Fahrenheit degrees. The value returned must be float value.
# Add the docstring in the function. Must return a float.
def convert_degrees(celsius_degree):
    # code goes here
    return
def convert_degrees(celsius_degree):
    return ((celsius_degree*1.8) + 32)