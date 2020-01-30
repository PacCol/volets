from flask import Flask, jsonify
app = Flask(__name__)

from flask import make_response
from flask import abort
from flask import request

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/volets/infos', methods=['GET'])
def get_infos():
    fichier_heure = open("heure.txt","r")
    heures = fichier_heure.read()
    fichier_heure.close()
    return jsonify({'infos':'gg'})

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
        print("ouverture")
        return jsonify({'status':'ouvert'})

    elif action == "fermer":
        print("fermeture")
        return jsonify({'status':'ferme'})

    elif "programmer_false" in action:
        print("programmation")
        fichier_heure = open("heure.txt","w")
        fichier_heure.write("heure:desactivated")
        fichier_heure.close()
        return jsonify({'status':'updated'})
