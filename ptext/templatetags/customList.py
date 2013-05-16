''' 
This class gives the ability to iterate
a dictionary in django template
'''
from django.template import Library

register = Library()

@register.filter
def get_original(self, index):
    '''returns original word'''
    return self.org[index]


@register.filter
def get_definition(self, index):
    '''returns definition'''
    return self.dfn[index]