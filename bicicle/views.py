from django.shortcuts import render
from decouple import config
import pyrebase

config = {
    "apiKey": config("API_KEY"),
    "authDomain": "biclicletasistemb.firebaseapp.com",
    "databaseURL": config("FIREBASE_URL"),
    "projectId": config("PROJECT_ID"),
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
    bicicle_stat_able = database.child('production').child('able').get().val()
    bicicle_stat_distance = database.child('production').child('distance').get().val()
    bicicle_stat_distanceParcial = database.child('production').child('distanceParcial').get().val()
    bicicle_stat_mode = database.child('production').child('mode').get().val()
    bicicle_stat_speed = database.child('production').child('speed').get().val()
    bicicle_stat_vMax = database.child('production').child('vMax').get().val()

    context = {
        'bicicle_stat_able': bicicle_stat_able,
        'bicicle_stat_distance': bicicle_stat_distance,
        'bicicle_stat_distanceParcial': bicicle_stat_distanceParcial,
        'bicicle_stat_mode': bicicle_stat_mode,
        'bicicle_stat_speed': bicicle_stat_speed,
        'bicicle_stat_vMax': bicicle_stat_vMax
    }

    if(request.GET.get('updateButton')):
        database.child('production').update({'able':bool(request.GET.get('AbleTextBox'))})
        database.child('production').update({'mode':int(request.GET.get('ModoTextBox'))})
        
    return render(request, 'bicicle/home.html', context)