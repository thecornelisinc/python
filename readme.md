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
    ==	Equal	 
        Example: x == y	

    !=	Not equal	
        Example: x != y	

    >	Greater than	
        Example: x > y	

    <	Less than	
        Example: x < y	

    >=	Greater than or equal to	
        Example: x >= y	

    <=	Less than or equal to	
        Example: x <= y

# python conditions and if statement
    - comparison operations are use together with if statement
    - if statement is denoted by "if" keyworld
    - the conditional statement, if, can be extended by Elif and Else 
    - You can check for more than one condition
 

# Python Loops
    - There are two type of Loops
        * For Loops
            - When you know the number of iteration
            - When you have a list or dictioinary of items
        * While Loops
            - When number of iteration is unknow 
            - When you need to repeat a block, action or instruction until a condition change

# continue and break
    * continue
        - Continue mean skip the current iteration/item and process from the next one
    * break
        - Break mean stop the the current, do not process with the next then exit the entire process

# Python Funtion 
    - A function is a block of code which only runs when it is called.
    - You can pass data, know as parameters into a function
    - A function can return data as a result
    - A parameter is the variable listed inside the parentheses in the function definition
    - An argument is the value that is sent to the function when it is called.

# Module    
    - What is a module?
        A module is like a package of code that contains related functions, variables, and instructions that can be reused in different parts of a program.
        For Examples:
        A module is just a file with some code inside it. If you have a file called math_tools.py that has functions for addition and subtraction, you can use this module in another program without writing the same code again

    -  There are several type of module: 

        Some are:
            * User-Defined/Custom Modules
            Modules that you create yourself to organize your code and make it reusable.
            Example: my_module_file.py

            * Built-in Module
            Pre-installed modules that come with a programming language like Python, JavaScript, or Java. They provide useful functions so you don’t have to write them from scratch
            Example:
                - random
                - datetime
                - math

            * External(Third-party Module)
            Modules developed by others that you can install and use in your project.
            - You must install this before import
            Example:
                - requests
                - json


    - importing and using module
        To use modul, you have to import it to the file where you want to use it from. Below are examples of ways you can use to import module
            - import module_name
            - from module_name import specific_function
            - import module_name as alias
            - from module_name import * (Not recommended)



# Summary
    - variables 
        - global
        - local
            * global x

    - varible
        - do and don't of variables name

    - data type
        - string
        - int
        - floor
        - complex
        - bool
        - list/array
        - dict/object

    - operators
    - comparism operators
    - conditional/if statement
    - loops
        * while 
        * for loop
    - function
        * def
            * argument
            * *arg
            * **key:pair
    - Modules