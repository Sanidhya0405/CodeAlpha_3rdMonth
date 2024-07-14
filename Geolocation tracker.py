import requests
import folium

def get_geolocation(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        return data
    else:
        return None

def create_map(lat, lon, location_name):
    map_ = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=location_name).add_to(map_)
    return map_

def main():
    ip_address = input("Enter the IP address: ")
    geolocation_data = get_geolocation(ip_address)
    
    if geolocation_data:
        lat = geolocation_data['lat']
        lon = geolocation_data['lon']
        location_name = geolocation_data['city']
        map_ = create_map(lat, lon, location_name)
        map_.save('map.html')
        print(f"Map has been saved as map.html. Location: {location_name}, Latitude: {lat}, Longitude: {lon}")
    else:
        print("Could not retrieve geolocation data.")

if __name__ == "__main__":
    main()
