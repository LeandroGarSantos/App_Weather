from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# In-memory data store
weather_data = [
    {'id': 1, 'city': 'San Francisco', 'temperature': 68, 'weather': 'Sunny'},
    {'id': 2, 'city': 'New York', 'temperature': 77, 'weather': 'Rainy'}
]

alerts_data = [
    {'id': 1, 'city': 'San Francisco', 'alert': 'Heat wave expected'},
    {'id': 2, 'city': 'New York', 'alert': 'Flash flood warning'}
]


# Weather Routes

@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)


@app.route('/weather/<int:id>', methods=['GET'])
def get_weather():
    for data in weather_data:
        if data['id'] == id:
            return jsonify(data)
    return jsonify({'error': 'Data not found'}), 404


@app.route('/weather', methods=['POST'])
def add_weather():
    new_data = request.get_json()

    new_id = 1
    if weather_data:
        new_id = max([weather['id'] for weather in weather_data]) + 1
    new_data['id'] = new_id

    weather_data.append(new_data)
    return jsonify(new_data), 201


@app.route('/weather/<int:id>', methods=['PUT'])
def update_weather(id):
    update_data = request.get_json()
    for data in weather_data:
        if data['id'] == id:
            data.update(update_data)
            return jsonify(data)
    return jsonify({'error': 'Data not found'}), 404


@app.route('/weather/<int:id>', methods=['DELETE'])
def delete_weather(id):
    for index, data in enumerate(weather_data):
        if data['id'] ==id:
            del weather_data[index]
            return jsonify({'message': 'Data deleted'})
    return jsonify({'error': 'Data not found'}), 404


#Alerts Routes

@app.route('/alerts', methods=['GET'])
def get_all_alerts():
    return jsonify(alerts_data)


@app.route('/alerts/<int:id>', methods=['GET'])
def get_alert(id):
    for data in alerts_data:
        if data['id'] == id:
            return jsonify(data)
    return jsonify({'error': 'Data not found'}), 404


@app.route('/alerts', methods=['POST'])
def add_alert():
    new_data = request.get_json()

    new_id = 1
    if alerts_data:
        new_id = max([alert['id'] for alert in alerts_data]) + 1
    new_data['id'] = new_id

    alerts_data.append(new_data)
    return jsonify(new_data), 201


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)