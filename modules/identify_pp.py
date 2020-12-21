# This module contains a function which will identify the hyperlink extension that 
# directs a user to a site's privacy policy, by checking the text 
# contained in the inner HTMl of any <a> tags

def find_pp(soup):
    
    # collect all hyperlinks to iterate over
    hyperlinks = soup.find_all("a")

    # use text in inner html to find privacy policy
    for link in hyperlinks:
        if link.text.lower() == "privacy policy":
            return link.attrs["href"]

