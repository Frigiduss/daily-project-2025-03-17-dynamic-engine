#!/usr/bin/env python3
'''
Main application file for this random project.
'''
import random
import sys

def main():
    '''Main function to run the application.'''
    print("Welcome to this randomly generated project!")
    print(f"Random number: {random.randint(1, 100)}")
    
    # Add some random functionality
    options = ["Option A", "Option B", "Option C"]
    print(f"Today's choice: {random.choice(options)}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
