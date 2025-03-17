'''
Utility functions for the project.
'''
import random
import string

def generate_random_string(length=10):
    '''Generate a random string of specified length.'''
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def calculate_something(a, b):
    '''Calculate something with two numbers.'''
    return a * b + random.randint(1, 10)
