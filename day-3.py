# Day 3: Formatting Strings and Processing User Input

# string conversion

int("25")

# basic string manipulations
"Hello, World!".lower()       # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"


# String format method

print("{} is {} years old!".format("Mano", "23"))

output = "{} is {} years old, and {} works as a {}."

print(output.format("John", 24, "John", "web developer"))

# with number placeholders
output = "{0} is {1} years old, and {0} works as a {2}."

print(output.format("John", 24, "web developer"))

# multiple times
user_name = " ROLF SMITH  ".strip().title()

