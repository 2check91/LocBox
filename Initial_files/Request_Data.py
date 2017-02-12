#Using Capital One API Request.

#import requests
import json

#url = "https://asdfasda-4bc1f.firebaseio.com/"
#data = requests.get(url).json()

#with open('idk.json', 'w') as outfile:
    #json.dump(data, outfile)


from firebase import firebase
firebase = firebase.FirebaseApplication('https://asdfasda-4bc1f.firebaseio.com/', '7325527269')
result = firebase.get('https://asdfasda-4bc1f.firebaseio.com/', '7325527269')

with open('idk.json', 'w') as outfile:
    json.dump(result, outfile)
