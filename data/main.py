import requests
url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
r = requests.get(url, allow_redirects=True)

open('facebook.ico', 'wb').write(r.content)
