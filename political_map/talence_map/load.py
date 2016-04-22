import os
from django.contrib.gis.utils import LayerMapping
from .models import Talence

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

talence_shp = os.path.abspath(os.path.join('talence_map', 'data', 'overlap_aggregate_data', 'overlap_aggregate_data.shp'))


def load_talence_data(verbose=True):
    lm = LayerMapping(Talence, talence_shp, talence_mapping,
                        transform=False, encoding='iso-8859-1')
    lm.save(verbose=verbose)













