"""
This is the models file for the parallel display.
There are no real models being used.
In any case, this entire module will soon be destroyed
"""
from django.db import models


class Languages(models.Model):
    '''Dictionary object'''
    fromLang = models.CharField(max_length=2)
    toLang = models.CharField(max_length=2)
    original = models.CharField(primary_key=True, max_length = 20)
    definition = models.CharField(max_length = 200)
    

'''
class UserDictionary(models.Model):
	fromLang = models.CharField(max_length=2)
	toLang = models.CharField(max_length=2)

class Languages(models.Model):
	fromLang = models.CharField(max_length=2)
	toLang = models.CharField(max_length=2)

	class Meta:
		unique_together = ('fromLang', 'toLang')
'''