import sys
import requests
from bs4 import BeautifulSoup

# Check if URL is provided
if len(sys.argv) != 2:
    print("Usage: python seir.py <URL>")
    sys.exit()

url = sys.argv[1]
header={'User-Agent': 'Mozilla/5.0'}

# Get webpage
try:
    response = requests.get(url,headers=header)

except:
    print("Error fetching the URL")
    sys.exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Title
if soup.title:
    print("Title page : \n",soup.title.text,"\n")
else:
    print("No Title")

# Body
if soup.body:
    body=soup.body.get_text(separator=" ",strip=True)
    print("Body page :\n",body,"\n")

else:
    print("No Body")

# Links
print("ALL Links : \n")
links=[]
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)
print(" ".join(links))


