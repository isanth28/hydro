from flask import Flask, jsonify, render_template
import requests

ESP32_IP = "10.243.175.9"

app = Flask(__name__)

# -----------------------------
# DASHBOARD
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -----------------------------
# AUTO CONTROL
# -----------------------------
@app.route('/auto_on')
def auto_on():
    try:
        requests.get(f"http://{ESP32_IP}/auto_on")
        return "AUTO STARTED"
    except:
        return "ESP32 ERROR"


@app.route('/auto_off')
def auto_off():
    try:
        requests.get(f"http://{ESP32_IP}/auto_off")
        return "AUTO STOPPED"
    except:
        return "ESP32 ERROR"


# -----------------------------
# PUMP CONTROL
# -----------------------------
@app.route('/pump_on')
def pump_on():
    try:
        requests.get(f"http://{ESP32_IP}/pump_on")
        return "PUMP ON"
    except:
        return "ERROR"


@app.route('/pump_off')
def pump_off():
    try:
        requests.get(f"http://{ESP32_IP}/pump_off")
        return "PUMP OFF"
    except:
        return "ERROR"


# -----------------------------
# GATE CONTROL
# -----------------------------
@app.route('/gate1_open')
def gate1_open():
    requests.get(f"http://{ESP32_IP}/gate1_on")
    return "Gate1 OPEN"


@app.route('/gate1_close')
def gate1_close():
    requests.get(f"http://{ESP32_IP}/gate1_off")
    return "Gate1 CLOSED"


@app.route('/gate2_open')
def gate2_open():
    requests.get(f"http://{ESP32_IP}/gate2_on")
    return "Gate2 OPEN"


@app.route('/gate2_close')
def gate2_close():
    requests.get(f"http://{ESP32_IP}/gate2_off")
    return "Gate2 CLOSED"


@app.route('/gate3_open')
def gate3_open():
    requests.get(f"http://{ESP32_IP}/gate3_on")
    return "Gate3 OPEN"


@app.route('/gate3_close')
def gate3_close():
    requests.get(f"http://{ESP32_IP}/gate3_off")
    return "Gate3 CLOSED"


@app.route('/gate4_open')
def gate4_open():
    requests.get(f"http://{ESP32_IP}/gate4_on")
    return "Gate4 OPEN"


@app.route('/gate4_close')
def gate4_close():
    requests.get(f"http://{ESP32_IP}/gate4_off")
    return "Gate4 CLOSED"


# -----------------------------
# GET DATA FROM ESP32
# -----------------------------
@app.route('/get_data')
def get_data():
    try:
        r = requests.get(f"http://{ESP32_IP}/data", timeout=2)
        data = r.json()
        data["status"] = "online"
        return jsonify(data)
    except:
        return jsonify({
            "status": "offline",
            "pump": 0,
            "auto": 0,
            "stage": 0,
            "flowRate": 0,
            "totalLiters": 0
        })


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)