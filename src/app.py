from flask import Flask
app = Flask(__name__)
from flask import Flask,jsonify

todos = [ 
    { "label": "My first task", "done": False } 
    ]

@app.route('/myroute', methods=['GET'], )
def hello_world():
    return 'Hello World'


@app.route('/todos', methods=['GET'])
def hello():
   json_text = jsonify(todos)
   return json_text


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)