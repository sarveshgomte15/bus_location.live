from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store bus data in memory (dictionary keyed by bus_id)
bus_data = {}


@app.route("/")
def home():
    return "🚍 Bus Location Live Server is Running!"


# ---------------- DRIVER APP ----------------
@app.route("/driver")
def driver():
    return render_template("driver.html")


@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.get_json()
    bus_id = data.get("bus_id", "default_bus")
    lat = data.get("latitude")
    lon = data.get("longitude")

    if bus_id and lat and lon:
        bus_data[bus_id] = {"latitude": lat, "longitude": lon}
        return jsonify({"status": "success", "message": f"Bus {bus_id} updated."})
    else:
        return jsonify({"status": "error", "message": "Missing bus_id or coordinates"}), 400


# ---------------- PASSENGER APP ----------------
@app.route("/passenger")
def passenger():
    return render_template("passenger.html")


@app.route("/get_location/<bus_id>", methods=["GET"])
def get_location(bus_id):
    if bus_id in bus_data:
        return jsonify({"bus_id": bus_id, "location": bus_data[bus_id]})
    else:
        return jsonify({"status": "error", "message": "Bus not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
