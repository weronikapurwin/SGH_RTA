
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def regula():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2')) 
    if num1 + num2 > 5.8:
        return '1'
    else:
        return '0'

if __name__ == '__main__':
    app.run(debug=True)
