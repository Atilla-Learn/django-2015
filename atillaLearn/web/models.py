from django.db import models

TYPES_CHOICE = (
		("conference", "Conférence"),
		("training", "Formation"),
		("talk", "Talktilla")
	)

# Create your models here.
class Item(models.Model):


	CONFERENCE = 0
	TRAINING = 1
	TALK = 2
	TYPES_CHOICE = (
		(CONFERENCE, "Conférence"),
		(TRAINING, "Formation"),
		(TALK, "Talktilla")
	)
	type = models.SmallIntegerField("Type", choices=TYPES_CHOICE)
	title = models.CharField("Titre",  max_length=250)
	date = models.DateField("Date de la présentation", null=True, blank=True)
	short = models.TextField("Courte description", blank=True)
	replay_id = models.CharField("Id du replay youtube",  max_length=50, blank=True)
	image = models.FileField(upload_to='images/', blank=True)

	def __str__(self):
		return self.get_type_display() + " " + self.title
