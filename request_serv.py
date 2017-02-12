import requests
import json

url = "https://asdfasda-4bc1f.firebaseio.com/"
data = requests.get(url).json()

with open('test_test_test.json', 'w') as outfile:
    json.dump(data, outfile)
