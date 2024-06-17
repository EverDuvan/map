from django.shortcuts import render
import folium
from .models import Location

def map_view(request):
    # Get all saved locations from the database
    locations = Location.objects.all()

    # Create a Folium map centered at a certain location
    map = folium.Map(location=[locations[0].latitude, locations[0].longitude], zoom_start=10)

    # Add markers for each location
    for location in locations:
        folium.Marker([location.latitude, location.longitude], popup=location.name).add_to(map)

    # Render the map within the view code
    map = map._repr_html_()

    return render(request, 'map.html', {'map': map})