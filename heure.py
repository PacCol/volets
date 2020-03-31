from astral import LocationInfo
from astral.sun import sun
import datetime
import time
from ouverture import *

while True:
    now = datetime.datetime.now()
    fichier = open("heure.txt","r")
    heure = fichier.read()
    fichier.close()
    if heure != "heure:desactivated" and heure != "heure:sunset_sunrise":
        heure_ouverture = int(heure.split("|")[0].split(":")[0])
        minute_ouverture = int(heure.split("|")[0].split(":")[1])
        heure_fermeture = int(heure.split("|")[1].split(":")[0])
        minute_fermeture = int(heure.split("|")[1].split(":")[1])
        if now.hour == heure_ouverture and now.minute == minute_ouverture:
            ouvrir()
            time.sleep(70)
        if now.hour == heure_fermeture and now.minute == minute_fermeture:
            fermer()
            time.sleep(70)

    if heure == "heure:sunset_sunrise":
        city = LocationInfo("Here", "France", "Europe/London", 48.77, 2.10)
        now = datetime.datetime.now()
        s = sun(city.observer, date=datetime.date(now.year, now.month, now.day))
        
        horaire_ouverture_minute = (s["sunrise"].hour + 2) * 60 + (s["sunrise"].minute + 15)
        horaire_fermeture_minute = (s["sunset"].hour + 2) * 60 + (s["sunset"].minute + 15)
        horaire_actuel_minute = now.hour * 60 + now.minute

        if horaire_actuel_minute == horaire_ouverture_minute:
            ouvrir()
            time.sleep(70)
        if horaire_actuel_minute == horaire_fermeture_minute:
            fermer()
            time.sleep(70)

    time.sleep(5)
