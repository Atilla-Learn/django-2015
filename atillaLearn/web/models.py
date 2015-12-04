from django.db import models

TYPES_CHOICE = (
		("conference", "Conférence"), 
		("training", "Formation"), 
		("talk", "Talktilla")
	)

# Create your models here.
class Item(models.Model):
	type = models.CharField("Type",choices=TYPES_CHOICE, max_length=30)
	title = models.CharField("Titre",  max_length=250)
	date = models.DateField("Date de la présentation", null=True, blank=True)
	short = models.TextField("Courte description", blank=True)
	replay_id = models.CharField("Id du replay",  max_length=50, blank=True)
