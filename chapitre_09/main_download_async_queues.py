import requests
import httpx
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings


async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file = await queue_download.get()
        url_log_file = f"{url}{log_file}"
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url_log_file)
            save_param = log_file,response.text
            queue_save.put_nowait(save_param)
        
        queue_download.task_done()

async def save(queue_save:asyncio.Queue):
    while True:
        log_file,log_content = await queue_save.get()
        with open(log_file,"w") as f:
            f.write(log_content)
        queue_save.task_done()

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_save_workers = 5

    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]

    tasks = []
    for i in range(nb_download_workers):
        t = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(t)

    for i in range(nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)

    for a in all_a:
        param = url,a
        queue_download.put_nowait(param)

    await queue_download.join()
    await queue_save.join()

    [t.cancel() for t in tasks]

    end = time.perf_counter()
    print(f"{end-start:.3}s")


if __name__ == '__main__':
    asyncio.run(main())
