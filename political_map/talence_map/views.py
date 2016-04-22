from django.shortcuts import render_to_response
from django.http import HttpResponse
from djgeojson.serializers import Serializer as GeoJSONSerializer
from .models import Talence


def talence_bdv(request): # need to review the naming issue here!
	bdv_data = Talence.objects.all()
	geojson_data = GeoJSONSerializer().serialize(bdv_data, use_natural_keys=True)
	return HttpResponse(geojson_data)