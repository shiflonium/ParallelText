"""
forms.py creates and defines the structure for the forms before displaying them
on the webpage. The register forms determines the requirements and behavior of
the input fields presented to the user.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import UserAccount

class AccountCreateForm(UserCreationForm):
    """
    UserAccountCreate creates the user account based on provided credentials.
    Required: Username, Password, Password Confirmation, and Native Language.
    Optional: Email Address, First Name, Last Name.
    """
    #def __init__(self):
        #pass

    #username = forms.CharField(
        #max_length = 30,
        #required = True,
        #label = 'Username',
    #)

    #password1 = forms.CharField(
        #widget=forms.PasswordInput,
        #max_length = 30,
        #required = True,
        #label = 'Password',
    #)

    #password2 = forms.CharField(
        #widget = forms.PasswordInput,
        #max_length = 30,
        #required = True,
        #label = 'Password (again)',
    #)

    email = forms.EmailField(
        max_length = 75,
        required = False,
        label = 'Email Address',
    )

    first_name = forms.CharField(
        max_length = 30,
        required = False,
        label = 'First Name',
    )

    last_name = forms.CharField(
        max_length = 30,
        required = False,
        label = 'Last Name',
    )

    native_lang = forms.ChoiceField(
        choices = UserAccount.native_lang_choices,
        required = True,
        label = 'Native Language'
    )

    class Meta:
        """
        Model metadata used to identify attributes in POST data when submitting
        a registration form. Required by register/views.py --> form =
        AccountCreateForm(request.Post). Throws error if removed.
        """
        def __init__(self):
            pass

        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'native_lang',
        )

    def save(self, commit=True):
        """
        Saves the submitted registration form into database because Django does
        not automatically do it for you.
        """
        if commit:
            user = super(AccountCreateForm, self).save(commit=False)
            #user.username = self.cleaned_data['username']
            #user.password1 = self.cleaned_data['password1']
            #user.password2 = self.cleaned_data['password2']
            #user.email = self.cleaned_data['email']
            #user.first_name = self.cleaned_data['first_name']
            #user.last_name = self.cleaned_data['last_name']
            user.save()

        return user

