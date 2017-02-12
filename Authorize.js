var admin = require("firebase-admin");

var serviceAccount = require("/Users/Alphabum/Python_Database/node_modules/firebase-admin/package.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://asdfasda-4bc1f.firebaseio.com"
});
