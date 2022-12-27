from django.db import models
import uuid
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.

class Encroachment_table(models.Model):

    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    encrt_id=models.CharField(max_length=50)
    # DEPARTMENT_CHOICES=Choices('Real Estate', 'Legal', 'Maintenance', 'Pipeline Integrity', 'Operation', 'Damage Prevention', 'Engineering')
    # DEPARTMENT_CHOICES = [(1, 'Real Estate'),
    #            (2, 'Legal'),
    #            (3, 'Maintenance'),
    #            (4, 'Pipeline Integrity'),
    #            (5, 'Operation'),
    #            (6,'Damage Prevention'),
    #            (7,'Engineering')
    #            ]

    # department=MultiSelectField(choices='DEPARTMENT_CHOICES',max_choices=7,max_length=7)
    STATUS_CHOICES = Choices('active', 'assigned','follow_up','resolved','audited','rejected')
    status = StatusField(choices_name='STATUS_CHOICES')

    # ENCRT_TYPE_CHOICES = Choices('Erosion', 'Large trees','Fences','Utility poles','Excavation','Water bodies/Water crossings')
    # ENCRT_TYPE_CHOICES = [(1, 'Erosion'),
    #            (2, 'Large trees'),
    #            (3, 'Fences'),
    #            (4, 'Utility poles'),
    #            (5, 'Excavation'),
    #            (6,'Water bodies/Water crossings')
    # ]

    # encrt_type= MultiSelectField(choices='ENCRT_TYPE_CHOICES',max_choices=6,max_length=6)

    region=models.CharField(max_length=50)
    subregion=models.CharField(max_length=50)
    encrt_size=models.FloatField()
    dist_coa=models.IntegerField()
    CRITICALITY_CHOICES = Choices('high', 'low')
    criticality=StatusField(choices_name='CRITICALITY_CHOICES')