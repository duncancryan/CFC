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

    # Create external resources dictionary
    external_resources = extract_resources.extract(soup)

    # Convert external resources to JSON
    ext_rec_json = json.dumps(external_resources, indent = 4)

    # Write to resources.json
    with open("resources.json", "w") as outfile:
        outfile.write(ext_rec_json)


    # Find Privacy Policy extension in index page
    pp_ext = identify_pp.find_pp(soup)

    # Combine with index URL to create full link to be soupified
    pp_url = index_url + pp_ext

    print(pp_url)
    
    

