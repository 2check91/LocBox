from firebase import firebase
firebase = firebase.FirebaseApplication('https://asdfasda-4bc1f.firebaseio.com/', None)
new_user = 

result = firebase.post('accounts', new_user)
print (result == None)
