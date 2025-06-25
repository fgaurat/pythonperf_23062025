import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings
from functools import partial

def requests_download_and_save(url,log_file):
    url_log_file = f"{url}{log_file}"
    response = requests.get(url_log_file,verify=False)
    with open(log_file,"w") as f:
        f.write(response.text)

# def get_result(url):
#     return requests.get(url,verify=False)


async def async_requests_download_and_save(url,log_file):
    url_log_file = f"{url}{log_file}"
    loop = asyncio.get_event_loop()
    # response = await loop.run_in_executor(None,get_result,url_log_file)

    get_function = partial(requests.get,url_log_file,verify=False)
    response = await loop.run_in_executor(None,get_function)
    
    with open(log_file,"w") as f:
        f.write(response.text)

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url,verify=False)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]

    all_coroutines=[]
    for log_file in all_a:
        all_coroutines.append(async_requests_download_and_save(url,log_file))

    await asyncio.gather(*all_coroutines)




    end = time.perf_counter()
    print(f"{end-start:.3}s")


if __name__ == '__main__':
    asyncio.run(main())
