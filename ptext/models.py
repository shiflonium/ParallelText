"""
This is the models file for the parallel display.
There are no real models being used.
In any case, this entire module will soon be destroyed
"""
from django.db import models


class Languages(models.Model):
    '''Dictionary object'''
    definitionID = models.IntegerField()
    fromLang = models.CharField(max_length=2)
    toLang = models.CharField(max_length=2)
    original = models.CharField(primary_key=True, max_length = 20)
    definition = models.CharField(max_length = 200)
    
    def save(self):
		top = Languages.objects.order_by('definitionID')

		if len(top) == 0:
			self.definitionID=0
			super(Languages, self).save()
		else:
			top = top[len(top)-1]
			self.definitionID = top.definitionID + 1
			super(Languages,self).save()


class UserDictionary(models.Model):
	userID = models.CharField(max_length=2)
	definitionID = models.CharField(max_length=2)

class AvailLangs(models.Model):
	fromLang = models.CharField(max_length=2)
	toLang = models.CharField(max_length=2)

	class Meta:
		unique_together = ('fromLang', 'toLang')
