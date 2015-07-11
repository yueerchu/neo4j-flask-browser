from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__)

neo4jAuth = requests.auth.HTTPBasicAuth('neo4j','password')
neo4jHost = 'http://localhost:7474'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/neo4j')
def test():
    r = requests.get(
        neo4jHost+'/user/neo4j', 
        auth=requests.auth.HTTPBasicAuth('neo4j','password'),
        )
    return jsonify(json.loads(r.text))

@app.route('/cypher', methods=['POST'])
def cypher():
    payload = request.get_json()
    r = requests.post(
        neo4jHost+'/db/data/transaction/commit',
        json={
          "statements" : [ payload ]
        },
        auth=neo4jAuth,
        headers={'Content-Type':'application/json'}
        )   
    return jsonify(json.loads(r.text)), r.status_code

@app.route('/labels')
def all_labels():
    r = requests.get(
        neo4jHost+'/db/data/labels',
        auth=neo4jAuth,
        )
    return jsonify(json.loads(r.text)), r.status_code

if __name__ == '__main__':
    app.run(debug=True)