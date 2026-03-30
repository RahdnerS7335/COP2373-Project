# ***************************************************************

# Author: Rahdner Savain
# Date: February 13, 2026
# Assignment: Programming Excercise 2

# Program Description:
# This program prompts user to enter an email message.
# The program scans the message for each of the 30 common spam keywords or phrases.
# Each occurrence of a spam keyword increases the spam score by 1 point.
# The program then calculates the "spam score" and displays the likelihood that the message is spam based on the "spam score"

# ***************************************************************


# Constant spam words/phrases

SPAM_WORDS = [
    "free", "win", "winner", "congratulations", "urgent",
    "act now", "limited time", "click here", "buy now",
    "order now", "risk free", "guarantee", "gift",
    "save big", "sweepstakes", "exclusive deal",
    "claim now", "no cost", "apply now", "fast cash",
    "extra income", "work from home", "earn money",
    "$$$", "investment opportunity", "prize",
    "lottery", "selected", "dear friend", "account suspended"
]


def calculateSpamScore(emailMessage):

    """
    Scans the user email message and calculates a spam score based on occurrences of spam keywords or phrases.

    Parameters:
    emailMessage (str) - the email message entered by user

    Variables:
    spamScore (int) - total spam score
    foundSpam (list) - spam keywords detected
    instance (int) - number of times keyword appears

    Logical Steps:
    1. Initialize spamScore and foundSpam
    2. Convert emailMessage to lowercase
    3. Loop through SPAM_WORDS
    4. Count each instance of each spam keyword
    5. Add instance to spamScore
    6. Store detected keywords into foundSpam list
    7. Return spamScore and foundSpam

    Returns:
    spamScore (int)
    foundSpam (list)
    """

    # Initialize spam score to zero
    spamScore = 0

    # Initialize detected keyword list
    foundSpam = []

    # Convert message to lowercase
    emailMessage = emailMessage.lower()

    # Loop through spam keywords constants
    for spamwrds in SPAM_WORDS:

        # Count occurrences of keyword
        instance = emailMessage.count(spamwrds)

        # Check if keyword are in message
        if instance > 0:

            # Increase spam score if found
            spamScore += instance

            # Add keyword found
            foundSpam.append(spamwrds)

    # Return results
    return spamScore, foundSpam


def spamLikelihood(rating):

    """
    Determines likelihood that email is spam based on spam score.

    Parameters:
    rating (int) - calculated spam score

    Variables:
    likelihood (str) - spam likelihood rating

    Logical Steps:
    1. Compare rating to spam keyword ranges
    2. Assign likelihood rating
    3. Return rating

    Returns:
    likelihood (str)
    """

    # Initialize likelihood variable
    likelihood = ""

    # Determine spam likelihood rating
    if rating == 0:
        likelihood = "Unlikely/Not a spam email"

    elif rating <= 5:
        likelihood = "Low chance of being a spam email"

    elif rating <= 10:
        likelihood = "Decent chance of being a spam email"

    elif rating >= 10:
        likelihood = "High chance of being a spam email"

    # Return likelihood rating
    return likelihood




# Initialize user input variable
emailMessage = ""

# Prompt user to enter email message
emailMessage = input("Enter the email message:")

# Call spamScore function
spamScore, spamwrds = calculateSpamScore(emailMessage)

# Call spamLikelihood function
likelihoodRating = spamLikelihood(spamScore)

# Display spam score
print("\n"+"Spam Score:", spamScore)

# Display likelihood rating
print("\n"+"Likelihood of spam?:", likelihoodRating)


# Check if spam words were found
if spamwrds:
    print("\n"+"Spam Words And/Or Phrases Found:")

    for word in spamwrds:
        print("*", word)
else:
 print("No spam words detected.")