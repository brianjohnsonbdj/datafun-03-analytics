"""
File: utils_Brian.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Brian Johnson
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variables (have a value True or False)
is_door_red: bool = False
has_international_clients: bool = True

# declare integer variables
numbers_of_doors: int = 5
years_in_operation: int = 10

# declare a floating point variables
average_height_of_doors_inches: float = 80.2
average_client_satisfaction: float = 4.7

# declare lists of strings
color_of_walls: list = ["red","blue","gray","teal"]
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# declare lists of numbers to illustrate statistics skills
width_of_each_door_inches: list = [62.1,60.0,55.5]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(width_of_each_door_inches)  
max_score: float = max(width_of_each_door_inches)  
mean_score: float = statistics.mean(width_of_each_door_inches)  
stdev_score: float = statistics.stdev(width_of_each_door_inches)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Is Door Red:                  {is_door_red}
Number of Doors:              {numbers_of_doors}
Color of Walls:               {color_of_walls}
Width of Each Door in Inches: {width_of_each_door_inches}
Minimum Width of the Door:    {min_score}
Maximum Width of the Door:    {max_score}
Mean Width of the Door:       {mean_score:.2f}
Standard Deviation of The Width of The Door: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_case.py")
    print(get_byline())
    print("END main() in utils_case.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()