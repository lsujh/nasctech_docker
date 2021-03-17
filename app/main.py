import ast
from flask import Flask, request

from handler import handler


app = Flask(__name__)

@app.route('/start/', methods=['GET'])
def index():
    req = request.args.get('', None)
    if req:
        try:
            data = ast.literal_eval(req)
        except:
            return "Incorrect data. Please enter data in the format: your_url/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}"
        return handler(data)
    return "No data. Please enter data in the format: your_url/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000, debug=True)