Integration Manager - Interview Task

geoip_loop.py:
 -Dohvata GeoIP podatke za prosledjenu IP adresu koristeci http://www.geoplugin.net/json.gp?ip=<ip-address>
 -Automatski ispisuje rezultat na svakih 60 sekundi
 -Pokretanje: python geoip_loop.py IPadresa

app.py:
 -Omogucava unos bilo koje IP adrese i prikaz GeoIP informacija preko GeoPlugin API
 -Pokretanje lokalno: python app.py
 -Pokretanje preko Dockera:
   docker build -t geoip-flask-app .	
   docker run -d -p 8080:8080 geoip-flask-app
