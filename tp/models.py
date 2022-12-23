from django.db import models

# Create your models here.
class Cinema(models.Model):
    nom = models.CharField(max_length=128)
    producteur = models.CharField(max_length=128)
    acteur = models.CharField(max_length=128)
    heure = models.TimeField()
    image = models.ImageField(upload_to="cinemas", blank=True, null=True)
    note = models.FloatField(default=0.0)
    synopsis = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom