from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyB36np7JlDbL0seQO3JUqyzoh2i5SEkx3E",
    "authDomain": "biclicletasistemb.firebaseapp.com",
    "databaseURL": "https://biclicletasistemb-default-rtdb.firebaseio.com",
    "projectId": "biclicletasistemb",
    "storageBucket": "biclicletasistemb.appspot.com",
    "messagingSenderId": "296685519501",
    "appId": "1:296685519501:web:a0f5ddc125e100c044d8c4"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

stats = [
    {
        'float': 4.05,
        'int': 5
    }
        
]

def home(request):
    bicicle_stat_float = database.child('test').child('float').get().val()
    bicicle_stat_int = database.child('test').child('int').get().val()
    
    context = {
        'bicicle_stat_float': bicicle_stat_float,
        'bicicle_stat_int': bicicle_stat_int
    }
    return render(request, 'bicicle/home.html', context)