from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/start_hunt')
def start_hunt():
    print("[ LegendsHub™ ] Web Trigger Received.")
    try:
        subprocess.Popen(['python', 'hunter.py'])
        return jsonify({"status": "Started", "message": "Hunting in progress..."})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})

@app.route('/get_results')
def get_results():
    try:
        with open("Legends_Gold.txt", "r") as f:
            data = [line.strip() for line in f.readlines()]
        return jsonify({"status": "Success", "data": data})
    except:
        return jsonify({"status": "Pending", "data": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

