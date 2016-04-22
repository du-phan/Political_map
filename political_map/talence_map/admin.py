from django.contrib import admin
from talence_map.models import Talence
from leaflet.admin import LeafletGeoAdmin 

admin.site.register(Talence, LeafletGeoAdmin)