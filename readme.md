# Introduction to Python

# What is Python?
Python is a popular programming language.

# Python Usecase:
It is used for:
    - web development (server-side),
    - software development,
    - mathematics,
    - system scripting.
    - Machime learning
    - Data analytics


# Python Installation
    - Check to see if you have python with:
        python --version
    - If not python is installed on your system, you can download and install here https://www.python.org/downloads/

# Where to write python code
1. In the terminal 
2. In a file with .py extension 
    example:
        helloworld.py

# write your first python code:
"Hello world!"

# How to execute python writen in a file
    use this command to run or execute your python code:
        python <file-name.py>


# introduction to print
    - Print is a built function, so you call it with parentheses. 
    - It is mainly use to display python code

# Python Basic requirement(!IMPORTANT)
1. python indentation
    - The spaces at the beginning of a code line.
    - The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# Python Comments
This can be use:
    - For xxplain Python code.
    - To make the code more readable.
    - To prevent execution when testing code.


# Introduction to Variables
    - Variables are containers for storing data values.
    - Rules for Variable Names:
        * Must start with a letter or the underscore character
        * A variable name cannot start with a number
        * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        * Variable names are case-sensitive (age, Age and AGE are three different variables)
        * A variable name cannot be any of the Python keywords.
    - variable can be global or local
    - A local variable can not be used by default outside of the function where it was declare
    - To use a local variable outside of the function where it was declare a "global <variable_name> must be define before the variable declaration"


# Intruduction to data type
    - An important concept
    - variable can store any data type
    - python has multiple data type such as
        * string/text as str
        * number as int, float and complex
        * boolean as bool
        * sequence as list, tuple and range
        * mapping as dict(dictionary)
        * set as set, frozenset
        * binary as byte, bytearray and memoryview
        * none as NoneType

    Use type() to know what the data type of a value is 
        example:
            type(x)
            type("name")
            type(4)

# Python Operators
    - Operators are used to perform operations on variables and values.

    Type of Operators: 
        * Arithmetic operators
        * Assignment operators
        * Comparison operators
        * Logical operators
        * Identity operators
        * Membership operators
        * Bitwise operators

# Python Comparison Operators
    ==	Equal	x == y	
    !=	Not equal	x != y	
    >	Greater than	x > y	
    <	Less than	x < y	
    >=	Greater than or equal to	x >= y	
    <=	Less than or equal to	x <= y