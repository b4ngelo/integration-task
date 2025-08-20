from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "GeoIP Fetcher is running"

@app.route("/geoip", methods=["GET"])
def geoip_lookup():
    ip = request.args.get("ip")
    if not ip:
        return jsonify({"error": "Missing 'ip' parameter"}), 400

    r = requests.get(f"http://www.geoplugin.net/json.gp?ip={ip}")
    if r.status_code == 200:
        return jsonify(r.json())
    else:
        return jsonify({"error": f"Request failed with status {r.status_code}"}), r.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
