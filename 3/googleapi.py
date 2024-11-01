import requests

API_KEY = 'AIzaSyAudMNmJ-wUGoZKtx61S3mh6GhvzBMCbHM'
LOCATION = "53.351222901222705, -6.2609904611237335"
RADIUS = 5000
TYPES = 'restaurant'

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={TYPES}&key={API_KEY}'
response = requests.get(url)
data = response.json()

print(data)