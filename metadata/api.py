import requests

# Define your Google API key
api_key = 'YOUR_API_KEY'

# Replace with your desired query latitude and longitude
query_latitude = 33.3448
query_longitude = -118.32648

# Define your desired search radius in meters
radius = 1000

# Make the API request to Google Places API
url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={query_latitude},{query_longitude}&radius={radius}&key={api_key}&type=restaurant|store'
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    results = response.json()

    # Extract and process the places data
    for place in results.get('results', []):
        name = place.get('name', 'N/A')
        location = place.get('geometry', {}).get('location', {})
        latitude = location.get('lat', 'N/A')
        longitude = location.get('lng', 'N/A')
        # You can print or store this information as needed
        print(f"Name: {name}, Latitude: {latitude}, Longitude: {longitude}")
else:
    print(f"Failed to retrieve data from Google Places API. Status code: {response.status_code}")
