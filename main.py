import requests
from bs4 import BeautifulSoup

def fetch_and_process(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the webpage
        title = soup.title.string

        # Print the title
        print("Title of the webpage:", title)
    else:
        print("Failed to fetch webpage. Status code:", response.status_code)

if __name__ == "__main__":
    # URL of the webpage to fetch
    url = "https://en.wikipedia.org/wiki/Main_Page"

    # Call the function to fetch and process the webpage
    fetch_and_process(url)
