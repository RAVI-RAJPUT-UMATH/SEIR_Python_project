import sys
import requests
from bs4 import BeautifulSoup

def main():
    # Check if URL is provided
    if len(sys.argv) != 2:
        print("Usage: python web_fetch.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)
        sys.exit(1)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # -------- PAGE TITLE --------
    print("PAGE TITLE:")
    if soup.title and soup.title.string:
        print(soup.title.string.strip())
    else:
        print("No title found")

    # -------- PAGE BODY TEXT --------
    print("\nPAGE BODY:")
    body = soup.body
    if body:
        text = body.get_text(separator="\n", strip=True)
        print(text)
    else:
        print("No body content found")

    # -------- LINKS --------
    print("\nLINKS:")
    links_found = False
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)
            links_found = True

    if not links_found:
        print("No links found on this page")

if __name__ == "__main__":
    main()
## this is my assignment of seir 