from flask import Flask, jsonify
app = Flask(__name__)

from flask import make_response
from flask import abort
from flask import request

from ouverture import *

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/volets/status', methods=['POST'])
def set_status():
    if not request.json:
        print("Not JSON")
        abort(400)

    if not 'action' in request.json:
        print("No action")
        abort(400)

    action = request.json['action']

    if action == "ouvrir":
        ouvrir()
        return jsonify({'status':'ouvert'})

    elif action == "fermer":
        fermer()
        return jsonify({'status':'ferme'})

    elif "programmer_false" in action:
        fichier_heure = open("heure.txt","w")
        fichier_heure.write("heure:desactivated")
        fichier_heure.close()
        return jsonify({'status':'updated'})

    elif "programmer_true" in action:
        heure_ouverture = action.split("(")[1].split(",")[0]
        minute_ouverture = action.split("(")[1].split(",")[1]
        heure_fermeture = action.split("(")[1].split(",")[2]
        minute_fermeture = action.split("(")[1].split(",")[3].split(")")[0]
        if minute_fermeture == "0":
            minute_fermeture = "00"
        heure = heure_ouverture + ":" + minute_ouverture + "|" + heure_fermeture + ":" + minute_fermeture
        fichier_heure = open("heure.txt","w")
        fichier_heure.write(heure)
        fichier_heure.close()
        return jsonify({'status':'updated'})
