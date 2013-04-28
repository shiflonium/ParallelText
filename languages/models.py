from django.db import models


class Languages(models.Model):
	langID =models.AutoField(primary_key=True)
	abbr = models.CharField(max_length=2)
	name = models.CharField(max_length=50)

	class Meta:
		unique_together = ('abbr', 'name')

class Translations(models.Model):
    '''Dictionary object'''
    definitionID = models.IntegerField()
    fromLang = models.ForeignKey(Languages, related_name='tran_from')
    toLang = models.ForeignKey(Languages, related_name='tran_to') 
    original = models.CharField(primary_key=True, max_length = 50)
    definition = models.TextField()
    #definition = models.CharField(max_length = 500)
    
    def save(self):
		top = Translations.objects.order_by('definitionID')

		if len(top) == 0:
			self.definitionID=0
			super(Translations, self).save()
		else:
			top = top[len(top)-1]
			self.definitionID = top.definitionID + 1
			super(Translations,self).save()
			


class UserDictionary(models.Model):
	userID = models.CharField(max_length=2)
	definitionID = models.CharField(max_length=2)

