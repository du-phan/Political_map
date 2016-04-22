"""political_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
from talence_map.models import Talence
from django.views.generic import TemplateView
from talence_map.views import talence_bdv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='talence/index.html'), name='home'),
	#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Talence), name='data'),
    url(r'^bdv.talence$', talence_bdv, name='talence')
]
