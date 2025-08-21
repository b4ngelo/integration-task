from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Minimalni web UI
@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>GeoIP Fetcher</title>
        </head>
        <body>
            <h2>GeoIP Fetcher</h2>
            <form id="geoForm">
                <input type="text" id="ip" placeholder="Enter IP" required>
                <button type="submit">Fetch GeoIP</button>
            </form>
            <pre id="result"></pre>
            <script>
                const form = document.getElementById('geoForm');
                form.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const ip = document.getElementById('ip').value;
                    try {
                        const res = await fetch(`/geoip?ip=${ip}`);
                        const data = await res.json();
                        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
                    } catch (err) {
                        document.getElementById('result').textContent = 'Error fetching data';
                    }
                });
            </script>
        </body>
    </html>
    """

# API endpoint
@app.route("/geoip", methods=["GET"])
def geoip_lookup():
    ip = request.args.get("ip")
    if not ip:
        return jsonify({"error": "Missing 'ip' parameter"}), 400

    try:
        r = requests.get(f"http://www.geoplugin.net/json.gp?ip={ip}", timeout=5)
        r.raise_for_status()
        return jsonify(r.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request failed: {e}"}), 500

if __name__ == "__main__":
    # Flask server spreman za Docker
    app.run(host="0.0.0.0", port=8080, debug=True)
