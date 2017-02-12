import http.client

conn = http.client.HTTPConnection("localhost:8000")
conn.request("POST", "/testurl")
conn.send("clientdata")
response = conn.getresponse()
conn.close()

print(response.read())
