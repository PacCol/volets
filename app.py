from flask import Flask, jsonify
app = Flask(__name__)

from flask import make_response
from flask import abort
from flask import request

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/volets/status', methods=['GET'])
def get_status():
    status_file = open("status.txt","r")
    status = status_file.read()
    status_file.close()
    return jsonify({'status':status})

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
        status_file = open("status.txt","w")
        status_file.write("ouvert")
        status_file.close()

    elif action == "fermer":
        print("fermeture")
        status_file = open("status.txt","w")
        status_file.write("fermer")
        status_file.close()
    
    status_file = open("status.txt","r")
    status = status_file.read()
    status_file.close()
    return jsonify({'status':status})
