import requests
import pandas as pd
import webbrowser

# Function to get latitude and longitude from a place name
def get_lat_lng_from_plz(plz):
    print(f"Fetiching location for code {plz}...")
    url = f"https://nominatim.openstreetmap.org/search?q={plz},Germany&format=json"
    response = requests.get(url)
    data = response.json()

    if data:
        lat = data[0]['lat']
        lng = data[0]['lon']
        return float(lat), float(lng)
    else:
        print(f"Location for code {plz} not found.")
        return None, None


# Get user input for postal codes
postal_codes = input("Enter a comma-separated list of German postal codes: ").split(',')
locations = [loc for code in postal_codes if (loc := get_lat_lng_from_plz(code.strip())) != (None, None)]

if not locations:
    print("No matching postal codes found")
else:
    df = pd.DataFrame(locations, columns=['lat', 'lng'])

    # Calculate the center point
    center_lat = df['lat'].mean()
    center_lng = df['lng'].mean()

    # open center location in maps
    # maps_url = f"https://www.google.com/maps/@{center_lat},{center_lng},15z"

    # Generate the Google Maps URL to place a pin at the center point
    maps_url = f"https://www.google.com/maps?q={center_lat},{center_lng}"

    print(f"Opening Google Maps at the center point: Latitude {center_lat}, Longitude {center_lng}")
    webbrowser.open(maps_url)
