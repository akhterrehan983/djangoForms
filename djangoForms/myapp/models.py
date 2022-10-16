from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class userForm(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

locationChoices = (
    ('Corporate Headoffice','Corporate Headoffice'),
    ('Operations Department', 'Operations Department'),
    ('Work Station','Work Station'),
    ('Marketing Division','Marketing Division'),
)
initialSeverityChoices = (
    ('Mild','Mild'),
    ('Moderate', 'Moderate'),
    ('Severe','Severe'),
    ('Fatal','Fatal'),
)
subIncidentTypesChoices = (('Environmental Incident', 'Environmental Incident'),
               ('Injury/Illness', 'Injury/Illness'),
               ('Property Damage', 'Property Damage'),
               ('Vehicle', 'Vehicle'))

class incidentReport(models.Model):
  location = models.CharField(max_length=30, choices=locationChoices, default="Corporate Headoffice")
  incidentDepartment = models.TextField(default=None,null=True)
  date = models.DateField(default=None,null=True)
  time = models.TimeField(default=None,null=True)
  incidentLocation = models.TextField(default=None,null=True)
  initialSeverity =  models.CharField(max_length=30, choices=initialSeverityChoices, default="Mild")
  suspectedCause = models.TextField(default=None,null=True)
  immediateAction = models.TextField(default=None,null=True)
  subIncidentTypes = MultiSelectField(choices=subIncidentTypesChoices,max_choices=4,
                                 max_length=30,null=True,blank=True)
  user = models.ForeignKey(userForm, on_delete=models.CASCADE,default=None)