import requests

r = requests.get("http://127.0.0.1:8000/student/api")

data = r.json()
print(data, type(data))