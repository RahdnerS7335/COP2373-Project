"""
------------------------------------------------------------
Author: Rahdner Savain
Date: March 21, 2026

Description:
This program allows the user to input a paragraph. It uses regular expressions with "look-ahead" to extract individual sentences, including those that begin with numbers.

Each sentence is displayed along with the total number of sentences in the paragraph.
------------------------------------------------------------
"""

# Import regular expression module
import re


def userParagraph():

    """
    Description: Prompts the user to enter a paragraph.

    Variables:
    paragraph (str) - user input text

    Logical Steps:
    1. Prompt user for paragraph input
    2. Store input
    3. Return paragraph

    Returns:
    paragraph (str)
    """

    # Prompt user for input
    paragraph = input("Enter a paragraph:\n")

    return paragraph


def getSentences(paragraph):

    """
    Description: Extracts sentences from a paragraph using regex  with look-ahead to properly detect sentence endings.

    Parameters:
    paragraph (str) - user input text

    Variables:
    pattern (str) - regex pattern for sentence extraction
    sentences (list) - list of extracted sentences

    Logical Steps:
    1. Define regex pattern
    2. Use re.findall() to extract sentences
    3. Return list of sentences

    Returns:
    sentences (list)
    """

    # Regex pattern using look-ahead
    # Matches sentences ending with . ! or ?
    # Ensures next sentence starts with capital letter OR number
    pattern = r'.+?[.!?](?=\s+[A-Z0-9]|$)'

    # Extract sentences using regex
    sentences = re.findall(pattern, paragraph, re.MULTILINE)

    return sentences



def displayResults(sentences):

    """
    Description: Displays each sentence and the total count.

    Parameters: sentences (list) - list of extracted sentences

    Variables: count (int) - number of sentences

    Logical Steps:
    1. Loop through sentences
    2. Print each sentence
    3. Count total sentences
    4. Display count

    Returns:
    None
    """

    # Initialize sentence count
    count = len(sentences)

    print("\nSentences:")

    # Loop and display each sentence
    for sentence in sentences:

        print("-", sentence.strip())


    # Display total count
    print("\nTotal Number of Sentences:", count)


def main():

    """
    Description: Controls program execution.

    Variables:
    paragraph (str)
    sentences (list)

    Logical Steps:
    1. Get paragraph input
    2. Extract sentences
    3. Display results

    """

    # Get user input
    paragraph = userParagraph()

    # Extract sentences
    sentences = getSentences(paragraph)

    # Display results
    displayResults(sentences)



# Start the program
main()