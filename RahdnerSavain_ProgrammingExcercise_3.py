"""
------------------------------------------------------------
Author: Rahdner Savain
Date: February 22, 2026
Program Name: Monthly Expense Analyzer

Description:
This program prompts the user to enter their monthly expenses
by expense type and amount. It then uses the reduce() method
to calculate the total expense, highest expense, and lowest
expense. The program also labels which expense category is
the highest and lowest.
------------------------------------------------------------
"""

import functools
from functools import reduce


# Expense
def get_expenses():
    """
    Description:
    Prompts the user to enter expense types and amounts and stores them in a list of tuples.

    Parameters:
    None

    Variables:
    expenses_list (list) - stores expense type (str) and amount (float)
    expense_type (str) - category of expense
    expense_amount (float) - cost of expense

    Logical Steps:
    1. Initialize empty expenses_list
    2. Prompt user for expense type
    3. Check if user enters 'done'
    4. Prompt for expense amount
    5. Store as tuple in list
    6. Repeat until finished
    7. Return expenses_list

    Returns:
    expenses_list (list)
    """

    # Initialize expense list
    expenses_list = []


    print("Enter your monthly expenses.")
    print("Type 'done' when you are finished.\n")

    while True:
        # Ask users for expense group type
        expense_type = input("Enter expense group type: ")

        # Type "done" to clear line and ask user if their is another group type to be added
        if expense_type.lower() == 'done':
            break

        # Ask users for amount
        expense_amount = float(input("Enter expense amount: $"))

        # Store the expense as a tuple (type, amount)
        expenses_list.append((expense_type, expense_amount))

        print()

    return expenses_list


# Calculates the total of expenses

def total_expenses(expenses):
    """
    Description:
    Uses reduce() to calculate the total of all
    expense amounts in the list.

    Parameters:
    expenses (list) - list of tuples containing expense type (str) and amount (float)

    Variables:
    total (float) - running sum of expenses
    item (tuple) - expense tuple from list

    Logical Steps:
    1. Use reduce() to iterate through expenses
    2. Add each expense amount
    3. Store total
    4. Return total

    Returns:
    total (float)
    """
    # Calculate total using reduce
    return reduce(lambda total, item: total + item[1], expenses, 0)


# Calculate the highest expense

def find_highest(expenses):
    """
    Description:
    Uses reduce() to determine the highest
    expense from the list.

    Parameters:
    expenses (list) - list of tuples containing expense type (str) and amount (float)

    Variables:
    a (tuple) - current highest expense
    b (tuple) - next expense in list

    Logical Steps:
    1. Compare expense amounts
    2. Keep the larger amount
    3. Repeat for all items
    4. Return highest tuple

    Returns:
    tuple (str, float)
    """

    # Find highest expense
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)


# Calculates the lowest expense
def find_lowest(expenses):
    """
    Description:
    Uses reduce() to determine the lowest expense from the list.

    Parameters:
    expenses (list) - list of tuples containing expense type (str) and amount (float)

    Variables:
    a (tuple) - current lowest expense
    b (tuple) - next expense in list

    Logical Steps:
    1. Compare expense amounts
    2. Keep the smaller amount
    3. Repeat for all items
    4. Return lowest tuple

    Returns:
    tuple (str, float)
    """

    # Find lowest expense
    return reduce(lambda a, b: a if a[1] < b[1] else b, expenses)


# Displays the total amount of expense and lists the highest & lowest expenses
def display_results(total, highest, lowest):
    """
    Description:
    Displays the total expense, highest expense, and lowest expense with labels.

    Parameters:
    total (float) - total expense amount
    highest (tuple) - highest expense
    lowest (tuple) - lowest expense

    Variables:
    None

    Logical Steps:
    1. Print total expenses
    2. Display highest expense type and amount
    3. Display lowest expense type and amount

    Returns:
    None
    """
    # Display results
    print("\n----- Expense Summary -----")
    print(f"Total Expenses: ${total:.2f}")
    print("Highest Expense:", highest[0], "- $", highest[1])
    print("Lowest Expense:", lowest[0], "- $", lowest[1])


# Main function
def main():
    """
    Description:
    Controls the execution of the expense analyzer program.

    Parameters:
    None

    Variables:
    expenses (list) - list of user expenses
    total_expense (float) - total expense
    highest_expense (tuple) - highest expense
    lowest_expense (tuple) - lowest expense

    Logical Steps:
    1. Call get_expenses()
    2. Check if list is not empty
    3. Call total_expenses()
    4. Call find_highest()
    5. Call find_lowest()
    6. Display results
    7. Print message if no data

    Returns:
    None
    """

    expenses = get_expenses()

    if len(expenses) != 0:
        # Calculate total expenses
        total_expense = total_expenses(expenses)
        # Get highest expense
        highest_expense = find_highest(expenses)
        # Get lowest expense
        lowest_expense = find_lowest(expenses)
        # Display results
        display_results(total_expense, highest_expense, lowest_expense)
        return

    print("No expenses were entered.")


# Call main function
main()