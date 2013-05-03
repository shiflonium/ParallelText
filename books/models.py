'''
This file defines the models for the books.
It includes 
(a) BookInfo:  (i)title, (ii) author, (iii) #chapters 
(b) BookTranslation: (i)language (ii) bookid 
                      (iii) translator (iv) copyright
'''
from django.db import models
from languages.models import Languages

# Create your models here.


class BookInfo (models.Model):
    '''
    (a) BookInfo:  (i)title, (ii) author, (iii) #chapters 
    '''
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=96)
    author = models.CharField(max_length=64)
    chaps = models.IntegerField()

class BookTranslation (models.Model):
    '''
    (b) BookTranslation: (i)language (ii) bookid 
    (iii) translator (iv) copyright
    '''
    id = models.AutoField(primary_key=True)    
    book_id  = models.ForeignKey(BookInfo)
    language_id = models.ForeignKey(Languages)
    translator_name = models.CharField(max_length=32)
    copyright_info = models.CharField(max_length=32)
