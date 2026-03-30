"""
------------------------------------------------------------
Author: Rahdner Savain
Date: March 7, 2026

Description:
This program validates user input for phone numbers,
social security numbers, and ZIP codes using regular
expressions. The user is prompted to enter each value
and the program determines if the input is valid.

The program also includes test examples to verify
that the validation functions correctly identify
valid and invalid inputs.
------------------------------------------------------------
"""

import re

# Pattern checks for three digits, a dash, three digits, another dash, and four digits
PHONE_PATTERN = r'\d\d\d-\d\d\d-\d\d\d\d$'

# Pattern checks for Social Security Number format XXX-XX-XXXX
SSN_PATTERN = r'\d\d\d-\d\d-\d\d\d\d$'

# Pattern checks for a standard 5 digit ZIP code
ZIP_PATTERN = r'\d\d\d\d\d$'


def validatePhone(phoneNumber):

    """
    Description: Validates a phone number using a regular expression.
    Expected format: XXX-XXX-XXXX

    Parameters:
    phoneNumber (str) - phone number entered by user

    Variables:
    match (Match object or None) - result from regex match

    Logical Steps:
    1. Compare phoneNumber with PHONE_PATTERN
    2. Check if match is found
    3. Return True if valid
    4. Return False if invalid

    """

    # Compare the user's phone number input against the phone pattern
    match = re.match(PHONE_PATTERN, phoneNumber)

    # If the pattern matches, return True; otherwise return False
    return match



def validateSSN(ssnNumber):

    """
    Description: Validates a Social Security Number using a regular expression.
    Expected format: XXX-XX-XXXX

    Parameters:
    ssnNumber (str) - SSN entered by user

    Variables:
    match (Match object or None) - result from regex match

    Logical Steps:
    1. Compare ssnNumber with SSN_PATTERN
    2. Check if match exists
    3. Return True if valid
    4. Return False if invalid

    """

    # Compare the user's SSN input against the SSN pattern
    match = re.match(SSN_PATTERN, ssnNumber)

    # Return True if a valid pattern match is found
    return match



def validateZip(zipCode):

    """
    Description: Validates a ZIP code using a regular expression.
    Expected format: XXXXX

    Parameters:
    zipCode (str) - ZIP code entered by user

    Variables:
    match (Match object or None) - result from regex match

    Logical Steps:
    1. Compare zipCode with ZIP_PATTERN
    2. Check if match exists
    3. Return True if valid
    4. Return False if invalid

    """

    # Compare the ZIP code input against the ZIP code pattern
    match = re.match(ZIP_PATTERN, zipCode)

    # Return True if the ZIP code matches the expected format
    return match

def main():

    """
    Description: Main function that collects user input and
    validates phone number, SSN, and ZIP code.

    Variables:
    phoneNumber (str) - user phone number
    ssnNumber (str) - user social security number
    zipCode (str) - user zip code

    Logical Steps:
    1. Prompt user for phone number
    2. Validate phone number
    3. Prompt user for SSN
    4. Validate SSN
    5. Prompt user for ZIP code
    6. Validate ZIP code
    7. Display validation results

    """

    # Initialize variables that will store user input values
    phoneNumber = ""
    ssnNumber = ""
    zipCode = ""


    # Ask the user to enter a phone number
    phoneNumber = input("Enter phone number (XXX-XXX-XXXX): ")

    if validatePhone(phoneNumber):

        print("Phone number is VALID")

    else:

        print("Phone number is INVALID")


    print()


    # Ask the user to enter their Social Security Number
    ssnNumber = input("Enter Social Security Number (XXX-XX-XXXX): ")

    if validateSSN(ssnNumber):

        print("SSN is VALID")

    else:

        print("SSN is INVALID")


    print()


    # Ask the user to enter their ZIP code
    zipCode = input("Enter ZIP code (XXXXX): ")

    if validateZip(zipCode):

        print("ZIP code is VALID")

    else:

        print("ZIP code is INVALID")


    # Display user inputs
    print("\nPhone Number Entered:", phoneNumber)

    print("SSN Entered:", ssnNumber)

    print("ZIP Code Entered:", zipCode)

    print()



# Call main function
main()