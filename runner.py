# Imports
import requests
import json
from bs4 import BeautifulSoup
import modules.extract_resources as extract_resources
import modules.word_count as word_count
import modules.identify_pp as identify_pp

# Assign root url to be scraped to variable
index_url = "https://www.cfcunderwriting.com"

# Request url and isolate content
index_result = requests.get(index_url, headers={"User-Agent": "Mozilla/5.0"})
index_content = index_result.content

# Check for legitimate response
if (index_result.status_code == 200):

    # Create BeautifulSoup Object for index url
    soup = BeautifulSoup(index_content, "html.parser")

    test = identify_pp.find_pp(soup)
    print(test)

