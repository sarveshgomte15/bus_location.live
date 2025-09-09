from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bus_data = {}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    bus_id = data.get("bus_id")
    lat = data.get("lat")
    lng = data.get("lng")
    bus_no = data.get("bus_no")
    driver_name = data.get("driver_name")

    bus_data[bus_id] = {
        "lat": lat,
        "lng": lng,
        "bus_no": bus_no,
        "driver_name": driver_name
    }
    return jsonify({"status": "success", "message": "Location updated"})

@app.route('/get_buses', methods=['GET'])
def get_buses():
    return jsonify(bus_data)

@app.route('/driver')
def driver_page():
    return render_template('driver.html')

@app.route('/passenger')
def passenger_page():
    return render_template('passenger.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
