import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url,verify=False)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]


    for log_file in all_a:
        url_log_file = f"{url}{log_file}"
        response = requests.get(url_log_file,verify=False)
        with open(log_file,"w") as f:
            f.write(response.text)

    end = time.perf_counter()
    print(f"{end-start:.3}s")


if __name__ == '__main__':
    main()
