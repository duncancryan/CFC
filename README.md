To run this program locally:

At the root:
- create a virtual environment with the command "python3 -m venv venv"
- to install the correct dependencies run "pip3 install -r requirements.txt"

(If you do not wish to use virtualenv, simply install beautifulsoup4 and requests globally using PIP)

then simply run "python3 runner.py" in the root directory. 
- This will generate two json files.


Some reflections upon review:

- An else cause should have been added to the main code block in the runner to warn the user and break if the response is bad (404, etc)

- I noticed a couple of scripts for google tag managers which did not have a "src" attribute, personally, I haven't worked with regular expression, so in the interest of saving time and getting a bit of an MVP done in the two hours given, I targeted the external resources with an "href" or "src" attribute to exploit. In retrospect I would have liked to have used Python's re library to pull some urls out of these script tags.

- Given time for a bit more of a once over at the end I would have pulled the process of splitting and cleaning the text for text-containing tags (in the count function in word_count) out into a separate helper function. 
    
- I spent a little bit too much time trying to figure out the most efficient way to get all of the text for the page. Inititally I was playing around with using get_text() on the "main" tag to try and cut down on code and processing, as well as a combination of get_text() and find_all(). I found that when I tried these methods a lot of unwanted characters were returned that the strip() method couldn't clean; hence, my targeting specific tags.