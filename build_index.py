import requests, json
from PIL import Image

response = requests.get('https://api.artic.edu/api/v1/artworks')
data = response.json()
print(json.dumps(data, indent = 2))