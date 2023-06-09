from flask import Flask, request, jsonify

app = Flask(__name__)

data = ""

# GET method
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

# POST method
@app.route('/data', methods=['POST'])
def post_data():
    new_data = request.json.get('data')
    if new_data:
        global data
        data = new_data
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'message': 'No data provided'})

# PUT method
@app.route('/data', methods=['PUT'])
def put_data():
    new_data = request.json.get('data')
    if new_data:
        global data
        data = new_data
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'message': 'No data provided'})

# DELETE method
@app.route('/data', methods=['DELETE'])
def delete_data():
    global data
    data = ""
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run()