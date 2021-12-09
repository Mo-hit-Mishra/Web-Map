import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lan = list(data["LAT"])
lon = list(data["LON"])
elve = list(data["ELEV"])


def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 3000 :
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=3, TileLayer="Mapbox Bright")

for lt, ln, el in zip(lan, lon, elve):
    map.add_child(folium.Marker(location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(colour_producer(el))))

map.save("Map1.html")
