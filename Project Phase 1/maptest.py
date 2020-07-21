import folium

my_map = folium.Map(location = [51.0485978122, -114.0701479559], zoom_start = 15)

folium.Marker([51.0485978122, -114.0701479559], popup = 'Traffic Volume').add_to(my_map)

my_map.save('Test_Map.html')