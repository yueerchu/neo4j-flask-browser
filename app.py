from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__, static_folder='templates/static')

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
    # payload = request.get_json()
    print(request.data)
    payload = request.data.decode()
    print('payload',type(payload),payload)
    r = requests.post(
        neo4jHost+'/db/data/transaction/commit',
        json={
          # "statements" : [ {"statement":"CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})"} ]
          "statements" : [ {"statement": payload} ]
        },
        auth=neo4jAuth,
        headers={'Content-Type':'application/json'}
        )   
    print(r.status_code)
    return jsonify(json.loads(r.text)), r.status_code

@app.route('/labels')
def all_labels():
    r = requests.get(
        neo4jHost+'/db/data/labels',
        auth=neo4jAuth,
        )
    return jsonify(json.loads(r.text)), r.status_code

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)