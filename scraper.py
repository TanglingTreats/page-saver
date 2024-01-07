import os
import requests
from bs4 import BeautifulSoup

# Create directory in current working directory
directory = "directory"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)

try :
    os.mkdir(path)
    print("Created '% s' directory" % directory)
except OSError as error:
    print(error)

# Init url
URL = "https://url.com"
file_name = "text.html"

while(True):
    print(file_name)
    page = requests.get(URL+"/"+file_name)

    # Parse content
    soup = BeautifulSoup(page.content, "html.parser")
    # Save page in target directory
    file = open(os.path.join(path, file_name), "w")
    file.write(soup.prettify())
    file.close()
    
    # Get next page element
    footer = soup.find('footer')
    next_elem = footer.find_all('a')
    # Base case
    if(len(next_elem) == 1):
        break
    # Set endpoint
    file_name = next_elem[0]['href']

print("Done")
