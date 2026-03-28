# print("Hello, JG")
import requests

# API url
# url = 'https://jsonplaceholder.typicode.com/todos/1'

# response = requests.get(url)
# print(response.json())
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.headers["Content-Type"])
# print(response.url)
# print(response.text)
# print(response.content)

# POST Method
# url = 'https://jsonplaceholder.typicode.com/todos'
# todo = {"userID": 1,"title": "Buy milk", "completed": False}
# header = {"Content-Type":"application/json"}
# response = requests.post(url, json=todo)
# print(response.json())
# print(response.status_code)


# PUT Method
# url = 'https://jsonplaceholder.typicode.com/todos/10'
# response = requests.get(url)
# print(response.json())


# url = 'https://jsonplaceholder.typicode.com/todos/10'
# todo = {"userID": 1,"title": "Wash car", "completed": True}
# header = {"Content-Type":"application/json"}
# response = requests.put(url, json=todo)
# print(response.json())
# print(response.status_code)


# PATH method
# url = 'https://jsonplaceholder.typicode.com/todos/10'
# todo = {"title": "Mow lawn"}
# header = {"Content-Type":"application/json"}
# response = requests.patch(url, json=todo)
# print(response.json())
# print(response.status_code)

# DELETE Method
url = 'https://jsonplaceholder.typicode.com/todos/10'
response = requests.delete(url)
print(response.json())
print(response.status_code)