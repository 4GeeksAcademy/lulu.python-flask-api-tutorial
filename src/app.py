from flask import Flask
from flask import request
app = Flask(__name__)
from flask import Flask,jsonify

todos = [ 
    { "label": "My first task", "done": False } 
    ]

@app.route('/myroute', methods=['GET'], )
def hello_world():
    json_text = jsonify(todos)
    return 'Hello World'


@app.route('/todos', methods=['GET'])
def hello():
   json_text = jsonify(todos)
   return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'

@app.route('/todos/<int:1>', methods=['DELETE'])
def delete_todo(int:1):
    print("This is the position to delete:", 1)
    return 'something'
    

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)