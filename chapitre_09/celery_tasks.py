from celery import Celery
import requests

app = Celery("tasks",broker="pyamqp://guest@localhost",backend="rpc://")

@app.task
def add(a,b):
    return a+b


@app.task
def download(url):
    log_file = url.split("/")[-1]
    response = requests.get(url)
    return log_file,response.text


@app.task
def save(args):
    log_file,log_content = args
    with open(log_file,"w") as f:
        f.write(log_content)
