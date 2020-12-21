# This module contains a function that will count the total words
# that appear on a page in text.

# Import
import itertools

def count(soup):
    
    # initialise variable for list of all text blocks (to later be joined into one list)
    all_text = []
    
    # find all tags to extract text from if it's there
    p_tags = soup.find_all("p")
    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")
    span_tags = soup.find_all("span")

    # iterate through and append any text to all_text
    for tag in p_tags:
        clean_text = tag.text.strip()
        split_text = clean_text.split(" ")
        all_text.append(split_text)
    
    for tag in h1_tags:
        clean_text = tag.text.strip()
        split_text = clean_text.split(" ")
        all_text.append(split_text)
    
    for tag in h2_tags:
        clean_text = tag.text.strip()
        split_text = clean_text.split(" ")
        all_text.append(split_text)
    
    for tag in span_tags:
        clean_text = tag.text.strip()
        split_text = clean_text.split(" ")
        all_text.append(split_text)

    
    # Inititalise empty flattened list
    flattened_text_list = []

    # Flatten, remove empty strings
    for group in all_text:
        for item in group:
            if item != "":
                flattened_text_list.append(item)
    
    return len(flattened_text_list)

    

