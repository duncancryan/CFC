# This module contains a function (extract_resources) that will scrape the origin
# url of each external resource loaded into the page, and populate a list within a dictionary object with these urls

def extract_resources(soup):
    # Initialise empty dictionary
    output = {}

    # Initialise url key/value pair
    output['urls'] = []

    # Find all <link> tags
    link_tags = soup.find_all("link")

    # Find all <img> tags
    img_tags = soup.find_all("img")

    # Find all <script> tags
    script_tags = soup.find_all("script")

    # Append href value from link tags to urls array in output dictionary
    for tag in link_tags:
        output['urls'].append(tag.attrs["href"])
    
    # Append src value from img tags to urls array in output dictionary
    for tag in img_tags:
        output['urls'].append(tag.attrs["src"])
    
    # Append src value from script tags to urls array in output dictionary
    for tag in script_tags:
        if tag.attrs["src"]:
            output['urls'].append(tag.attrs["src"])

    return output

    

