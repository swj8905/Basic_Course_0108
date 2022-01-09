from folium import Map

map = Map(location=[37.49789438056151, 127.0276811709592], zoom_start=17)
map.save("./map.html")