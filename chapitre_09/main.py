import requests
from bs4 import BeautifulSoup
from pprint import pprint

def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]

    pprint(all_a)



if __name__ == '__main__':
    main()
