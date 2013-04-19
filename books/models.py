from django.db import models
from ptext.models import AvailLangs

# Create your models here.


class BookInfo (models.Model):
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=96)
    author = models.CharField(max_length=64)
    numChaps = models.IntegerField()

class BookTranslation (models.Model):
    id = models.AutoField(primary_key=True)    
    book_id  = models.ForeignKey(BookInfo)
    language_id = models.ForeignKey(AvailLangs)
    translator_name = models.CharField(max_length=32)
    copyright_info = models.CharField(max_length=32)
