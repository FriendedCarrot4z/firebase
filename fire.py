import pyrebase

#The configuration key for my firebase
config = {
    "apiKey": "AIzaSyDaVzHzwo2kwpf6dfubn9vTu5Whf8pMmx4",
    "authDomain": "fir-test-d4ea4.firebaseapp.com",
    "databaseURL": "https://fir-test-d4ea4.firebaseio.com",
    "projectId": "fir-test-d4ea4",
    "storageBucket": "fir-test-d4ea4.appspot.com",
    "messagingSenderId": "1062772095092",
    "appId": "1:1062772095092:web:aeb21eea0170c52149f921",
    "measurementId": "G-V58KG97H1J"
  }

#Authorizations for firebase and set up  
firebase = pyrebase.initialize_app(config)
dataB = firebase.database()
auth = firebase.auth()
store = firebase.storage()

#asks if you have a login for the cloud
login = input("Please enter y if you have an account or n if you don't: ")
yes = True
while yes:
  if login == 'y': #allows you to sign into the cloud
      email = input("Please enter your email address: ")
      password = input("Please enter your password: ")
      reset = input("If you wish to reset your password enter 1, if not enter 2: ")
      if reset == '1':#if you wish to reset your email 
        auth.send_password_reset_email(email)
        print("We sent a reset to your email")
      else:
        signin = auth.sign_in_with_email_and_password(email, password)
        print("Sign in worked")
  elif reset == '2':#Allows you to create an account
    email = input("Please enter your email address: ")
    password = input("Please enter your password: ")
    user = auth.create_user_with_email_and_password(email, password)
    print("Created User is done")
    signin = auth.sign_in_with_email_and_password(email, password)
    print("Sign in worked")
    auth.send_email_verification(signin['idToken'])
    print("Verification has been sent")
  yes = False


#allows for you to upload or download a picture from the cloud. 
image = True
while image:
  pictures = input("If you want to insert a picture into the cloud enter 1 to download enter 2: ")
  if pictures == '1':
    name = input("enter the name of picture you wish to add, include the .type: ")
    store.child("images", name).put(name)
    print("Image uploaded")
  elif pictures == '2':
    name = input("enter the name of picture you wish to download, include the .type: ")
    rename = input("What do you wish to rename it?(have to rename for it to work): ")
    store.child("images", name).download(rename)
    print("Image downloaded")
  again = input("Do you want to download/upload more pictures? y/n ")
  if again == 'y':
    image = True
  elif again == 'n':
    image = False

















"""
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/8.0.0/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/8.0.0/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyDaVzHzwo2kwpf6dfubn9vTu5Whf8pMmx4",
    authDomain: "fir-test-d4ea4.firebaseapp.com",
    databaseURL: "https://fir-test-d4ea4.firebaseio.com",
    projectId: "fir-test-d4ea4",
    storageBucket: "fir-test-d4ea4.appspot.com",
    messagingSenderId: "1062772095092",
    appId: "1:1062772095092:web:aeb21eea0170c52149f921",
    measurementId: "G-V58KG97H1J"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>
"""