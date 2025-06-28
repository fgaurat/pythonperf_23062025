# Python, perfectionnement du 23/06




https://github.com/fgaurat/pythonperf_23062025

## Vidéo 1
https://youtu.be/6MhwWAVqEuo

## Vidéo 2
https://youtu.be/41iwWUi8jfE

Frédéric Gaurat


https://realpython.com/
https://daily.dev/fr-fr
https://www.cursor.com/
https://windsurf.com/editor
cline extension vs code


https://v0.dev/
https://bolt.new/
https://lovable.dev/




https://wiki.python.org/moin/TimeComplexity


https://refactoring.guru/fr


https://peps.python.org/pep-0000/

https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops





https://docs.python.org/3.13/library/functools.html#functools.wraps

https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)

https://www.mockaroo.com/
https://docs.python.org/3/library/csv.html#csv.DictReader


https://sqlitebrowser.org/dl/


```sql
CREATE TABLE "customers_tbl" (
	"id"	INTEGER,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"gender"	TEXT,
	"ip_address"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```
https://docs.python.org/3/library/sqlite3.html



https://logs.eolem.com/


https://n8n.io/


```
	"Python main": {
		"prefix": "pymain",
		"body": [
			"def main():",
			"\tpass$1",
			"",
			"if __name__ == '__main__':",
			"\tmain()",
		],
		"description": "Python main"
	}
```  
https://docs.python.org/3/tutorial/stdlib.html#internet-access


https://gitignore.io/


pip install requests
pip install beautifulsoup4
    

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start


https://docs.python.org/3/library/multiprocessing.html#introduction


https://docs.python.org/fr/3/library/concurrent.futures.html#threadpoolexecutor-example


https://docs.python.org/3/library/asyncio.html

http://latentflip.com/loupe/?code=JC5vbignYnV0dG9uJywgJ2NsaWNrJywgZnVuY3Rpb24gb25DbGljaygpIHsKICAgIHNldFRpbWVvdXQoZnVuY3Rpb24gdGltZXIoKSB7CiAgICAgICAgY29uc29sZS5sb2coJ1lvdSBjbGlja2VkIHRoZSBidXR0b24hJyk7ICAgIAogICAgfSwgMjAwMCk7Cn0pOwoKY29uc29sZS5sb2coIkhpISIpOwoKc2V0VGltZW91dChmdW5jdGlvbiB0aW1lb3V0KCkgewogICAgY29uc29sZS5sb2coIkNsaWNrIHRoZSBidXR0b24hIik7Cn0sIDUwMDApOwoKY29uc29sZS5sb2coIldlbGNvbWUgdG8gbG91cGUuIik7!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D


https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio


https://www.python-httpx.org/


https://www.python-httpx.org/async/


https://docs.celeryq.dev/en/stable/



https://docs.celeryq.dev/en/stable/getting-started/introduction.html#get-started

https://hub.docker.com/


docker pull rabbitmq
docker run -d -p 5672:5672 rabbitmq
docker ps  

# docker pull rabbitmq
```
docker run -d -p 5672:5672 rabbitmq
```
# pour Windows : 
```
celery -A celery_tasks worker --loglevel=INFO -P solo 
```

# pour les autres 
```
celery -A celery_tasks worker --loglevel=INFO
```



https://flask.palletsprojects.com/en/stable/quickstart/

https://flask.palletsprojects.com/en/stable/installation/
```
@app.route("/")
def index():
    html="<table>"
    dao = CustomerDAO('customers.db')
    customers = dao.find_all()
    for customer in customers:
        html+=f"""<tr>
        <td>{customer.id}</td>
        <td>{customer.first_name}</td>
        <td>{customer.last_name}</td>
        <td>{customer.gender}</td>
        <td>{customer.ip_address}</td>
        </tr>"""
    html+="</table>"
    return html
```    
## Emmet
```
div#toto.tutu.tata>ul>li*3
```

https://getbootstrap.com/

https://bubble.io/


https://www.figma.com/fr-fr/


https://streamlit.io/


https://docs.streamlit.io/get-started/installation



streamlit run main_streamlit.py


https://docs.streamlit.io/develop/api-reference/widgets/st.text_input


https://fastapi.tiangolo.com/#installation


https://www.usebruno.com/
https://www.postman.com/
https://insomnia.rest/

https://colab.research.google.com/notebooks/

pip install numpy pandas scikit-learn matplotlib

https://www.youtube.com/c/MachineLearnia





