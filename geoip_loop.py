import requests
import time
import sys

def fetch_geoip(ip_address: str):
    """Fetch GeoIP podaci za datu IP address sa geoplugin API."""
    url = f"http://www.geoplugin.net/json.gp?ip={ip_address}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}")
        return None

def main():
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
    else:
        ip_address = "8.8.8.8"

    print(f"Fetching GeoIP info for IP: {ip_address}")
    while True:
        geo_data = fetch_geoip(ip_address)
        if geo_data:
            print("\n--- GeoIP Result ---")
            for key, value in geo_data.items():
                print(f"{key}: {value}")
        else:
            print("No data received.")

        print("\nSleeping for 60 seconds...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
