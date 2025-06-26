import requests
import httpx
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings


async def async_httpx_download_and_save(url,log_file):
    url_log_file = f"{url}{log_file}"

    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url_log_file)

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
        all_coroutines.append(async_httpx_download_and_save(url,log_file))

    await asyncio.gather(*all_coroutines)




    end = time.perf_counter()
    print(f"{end-start:.3}s")


if __name__ == '__main__':
    asyncio.run(main())
