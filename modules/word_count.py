# This module contains a function that will count the total words
# that appear on a page in text.

def count(soup):
    
    # initialise variable for list of all text blocks (to later be joined into one list)
    all_text = soup.get_text()
    return all_text

