"""
This is the models file for the parallel display.
There are no real models being used.
In any case, this entire module will soon be destroyed
"""
from django.db import models


class HE_2_EN(models.Model):
    '''Dictionary object'''
    original = models.CharField(primary_key=True, max_length = 20)
    definition = models.CharField(max_length = 200)