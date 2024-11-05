from django.db import models

class DataEntry(models.Model):
    intensity = models.FloatField(null=True, blank=True)
    likelihood = models.FloatField(null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    topics = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    pest = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    swot = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.topics}"
