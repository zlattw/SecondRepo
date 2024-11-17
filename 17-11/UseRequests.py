import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
# print(type(response.content))
#
# print(response.text)

response2 = requests.post("https://httpbin.org/post",
                          data = "Test data",
                          headers ={"h1": "Test title"})
print(response2.text)