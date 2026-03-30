"""
This program has set amount of tickets and allows buyers to purchase pre-sells of the  limited number of tickets.
Each buyer can buy a maximum of 4 tickets.
20 tickets can be sold in total.
The program tracks the remaining tickets and counts the total number of buyers.
"""

# Constant for maximum tickets
MAX_TICKETS = 20

# Constant for maximum tickets per buyer
MAX_PER_BUYER = 4

def tickets_sold():
    """
    Controls the ticket-selling process until all tickets are sold.

    Variables:
        ticketsRemaining: number of tickets still available
        buyerCount: counting total buyers
        buyTickets: number of tickets want to be bought by buyer

    Logical Steps:
        1. Initialize Max_Tickets and Max_Per_Buyer constants
        2. Loop while the remaining tickets are sold
        3. Prompt user for number of tickets wants to buy
        4. Check request using if statements to determine remaining tickets
        5. Subtract tickets from tickets remaining and update buyer count
        6. Display remaining tickets
        7. Display total buyers when finished
    """

    # Initialize tickets remaining
    ticketsRemaining = MAX_TICKETS

    # Initialize buyer counter
    buyerCount = 0

    # Continue selling until tickets are gone
    while ticketsRemaining > 0:

        # Asks user for number of tickets wants to be bought
        buyTickets = int(input("How many tickets do you want to buy? (Max of 4): "))

        # Check to see if user inputs a # within range (1-4)
        if buyTickets < 1 or buyTickets > MAX_PER_BUYER:
            print("You can only buy 1 to 4 tickets.")

        # Check to see if enough tickets remain
        elif buyTickets > ticketsRemaining:
            print("Not enough tickets to remain.")

        else:
            # Subtract purchased tickets from remaining tickets left
            ticketsRemaining -= buyTickets

            # Add to buyer counter
            buyerCount += 1

            # Display remaining tickets
            print("Tickets remaining:", ticketsRemaining)

    # Display total buyers once tickets are sold out
    display_results(buyerCount)


def display_results(buyerCount):
    """
    Displays the total number of buyers.

    Parameters:
        buyerCount (int): total number of buyers

    Logical Steps:
        1. Display final buyer count

    Return:
        The total number of buyers
    """

    print("\nTickets sold out.")
    print("Total number of buyers:", buyerCount)


# Call the main function
tickets_sold()
