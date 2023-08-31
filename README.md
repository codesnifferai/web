## How to use it

```bash
$ # Get the code
$ git clone https://github.com/elsvital/codesnifferai.git
$ cd codesnifferai
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the home app in browser: http://127.0.0.1:8000/
```

## API Rest
- Url:  http://localhost:8000/api/v1/codesnifferai/
```bash
# Execute by Curl
curl --location 'http://localhost:8000/api/v1/codesnifferai/' \
--header 'Content-Type: application/json' \
--data '{
    "code": "code to analise"
}'
# By Python Request
import requests
import json

url = "http://localhost:8000/api/v1/codesnifferai/"

payload = json.dumps({
  "code": "code to analise"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# By Python Client

import http.client
import json

conn = http.client.HTTPSConnection("localhost", 8000)
payload = json.dumps({
  "code": "code to analise"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/v1/codesnifferai/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8")) 

```