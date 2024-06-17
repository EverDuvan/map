import folium
from django.shortcuts import render
from .models import Location

def map_view(request):
    # Get all saved locations from the database
    locations = Location.objects.all()

    if not locations:
        # Handle the case when there are no locations
        map = folium.Map(location=[0, 0], zoom_start=2)
    else:
        # Create a Folium map centered at the first location
        map = folium.Map(location=[locations[0].latitude, locations[0].longitude], zoom_start=10)

        # Add markers for each location
        for location in locations:
            popup_content = f"<b>{location.name}</b><br>{location.description}"
            folium.Marker([location.latitude, location.longitude], popup=popup_content).add_to(map)

    # Render the map within the view code
    map = map._repr_html_()

    return render(request, 'map.html', {'map': map})
