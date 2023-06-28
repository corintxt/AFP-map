import json
import requests

r = requests.get('https://www.afp.com/en/afp/map/getoffice/427')

office_list = r.json()
off = office_list['offices']

# Convert JSON entry for office to GeoJSON Feature
def office_to_geojson_feature(office_json):
    name = office_json['location_city']
    latitude = float(office_json['location_latitude'])
    longitude = float(office_json['location_longitude'])
    
    oj = {"type": "Feature",
          "geometry": 
           {"type": "Point",
            "coordinates": [longitude, latitude]
          },
            "properties": 
             {"name": name}
        }
    
    return oj

# Build list of office GeoJSON Features
offices = []
for o in off:
    offices.append(office_to_geojson_feature(o))

# Group together as GeoJSON FeatureCollection
office_geojson =  {
       "type": "FeatureCollection",
       "features": offices
}

# Save file and close
with open("AFP_France_offices.geojson", 'w') as f:
    json.dump(office_geojson, f)
f.close()