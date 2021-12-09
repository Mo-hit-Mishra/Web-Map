import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elve = list(data["ELEV"])
name = list(data["NAME"])


def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=4, TileLayer="Mapbox Bright")
fgv = folium.FeatureGroup(name='volcanoes')
for lt, lo, el in zip(lat, lon, elve):
    fgv.add_child(folium.CircleMarker(location=[lt, lo], radius=6, popup=str(el) + " m", fill_color=colour_producer(el),color='white',
    fill_opacity=0.7))
    
fgp = folium.FeatureGroup(name='population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green'
if x['properties']['POP2005'] < 10000000 else 'orange'if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map2.html")
