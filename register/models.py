"""
models.py defines the data and behavior that is being stored in the database.
The register models contains how the user account information should be stored.
"""
from django.db import models

class UserAccount(models.Model):
    """
    UserAccount stores the account settings for the user.
    This is an extension of the user_auth table in the database.
    """
    user = models.OneToOneField('auth.User', primary_key=True)

    # Language Codes
    # http://msdn.microsoft.com/en-us/library/ms533052%28v=vs.85%29.aspx
    # http://www.lingoes.net/en/translator/langcode.htm
    native_lang_choices = (
        ('en',  'English'),
        ('he',  'Hebrew'),
        ('es',  'Spanish'),
    )

    native_lang = models.CharField(
        blank=False,
        max_length = 2,
        choices = native_lang_choices,
        default = 'es',
    )


