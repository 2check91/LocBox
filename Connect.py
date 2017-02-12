from firebase import firebase
firebase = firebase.FirebaseApplication('https://asdfasda-4bc1f.firebaseio.com/', None)
result = firebase.get('/users', None)
print (result)
