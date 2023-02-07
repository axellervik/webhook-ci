from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

list = ['AAAAAAAAAAAAAa', 'Bunny', 'Cat', 'Duck', 'E']

@app.route('/', methods=['GET'])
def test1():
    if not request.is_json:
        return render_template('index.html')
    json_data = request.get_json()
    return json_data
    return jsonify({'GET': [item for item in list]})

@app.route('/', methods=['POST'])
def test2():
    return jsonify(request.form['payload'])
    if not request.is_json:
        return "fuck off post"
    json_data = request.get_json()
    # payload = req.json
    
    return "json data received"
    return jsonify({'POST': [item for item in list]})

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)
