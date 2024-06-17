from django.contrib import admin
from django.urls import path
from map_app.views import map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_view, name='map_view'),
]
