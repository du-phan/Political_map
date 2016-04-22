from __future__ import unicode_literals
# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Talence(models.Model):
    bdv_id = models.IntegerField()
    population = models.FloatField()
    agriculteu = models.FloatField()
    artisans = models.FloatField()
    cadres = models.FloatField()
    prof_inter = models.FloatField()
    employes = models.FloatField()
    ouvriers = models.FloatField()
    chomeurs = models.FloatField()
    retraites = models.FloatField()
    proprietai = models.FloatField()
    immigrant = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    @property
    def iris_name(self): 
        return self.nom_iris

# Auto-generated `LayerMapping` dictionary for Talence model
talence_mapping = {
    'bdv_id' : 'bdv_id',
    'population' : 'Population',
    'agriculteu' : 'Agriculteu',
    'artisans' : 'Artisans',
    'cadres' : 'Cadres',
    'prof_inter' : 'Prof_inter',
    'employes' : 'Employes',
    'ouvriers' : 'Ouvriers',
    'chomeurs' : 'Chomeurs',
    'retraites' : 'Retraites',
    'proprietai' : 'Proprietai',
    'immigrant' : 'Immigrant',
    'geom' : 'MULTIPOLYGON',
}
