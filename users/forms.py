"""
forms.py creates and defines the structure for the forms before displaying them
on the webpage. The register forms determines the requirements and behavior of
the input fields presented to the user.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserAccount
from languages.models import Languages

class AccountCreateForm(UserCreationForm):
    """
    AccountCreateForm provides the form model that creates the user account
    based on provided credentials.
    Required: Username, Password, Password Confirmation, and Native Language.
    Optional: Email Address, First Name, Last Name.
    """
    #def __init__(self):
        #pass

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

    native_lang = forms.ModelMultipleChoiceField(
        widget = forms.Select,
        queryset = Languages.objects.all().values_list('name', flat=True),
        label = 'Native Language'
    )

    #learn_lang = forms.ModelChoiceField(
        #widget = forms.Select,
        #queryset = Languages.objects.all(),
        #label = 'Learning Language'
    #)

    class Meta:
        """
        Model metadata used to identify attributes in POST data when submitting
        a registration form. Required by users/views.py --> form =
        AccountCreateForm(request.Post). Throws error if removed.
        """
        def __init__(self):
            pass

        model = UserAccount
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'native_lang',
            #'learn_lang',
        )



class AccountManageForm(forms.ModelForm):
    """
    AccountManageForm provides the form model that retrieves and displays the
    user's information based on the data already stored in the database.
    """
    #def __init__(self):
        #pass

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

    native_lang = forms.ModelChoiceField(
        widget = forms.Select,
        queryset = Languages.objects.all(),
        label = 'Native Language'
    )

    #learn_lang = forms.ModelChoiceField(
        #widget = forms.Select,
        #queryset = Languages.objects.all(),
        #label = 'Learning Language'
    #)

    class Meta:
        """
        Model metadata used to identify attributes in POST data when submitting
        a registration form. Required by users/views.py --> form =
        AccountCreateForm(request.Post). Throws error if removed.
        """
        def __init__(self):
            pass

        model = UserAccount
        fields = (
            'email',
            'first_name',
            'last_name',
            'native_lang',
            #'learn_lang',
        )



class AccountManagePassForm(forms.ModelForm):
    """
    AccountManagePassForm provides the form model that allows the user to
    change their account password.
    """
    #def __init__(self):
        #pass

    pass_old = forms.CharField(
        widget=forms.PasswordInput,
        max_length = 30,
        required = True,
        label = 'Old Password',
    )

    pass_new1 = forms.CharField(
        widget = forms.PasswordInput,
        max_length = 30,
        required = True,
        label = 'New Password',
    )

    pass_new2 = forms.CharField(
        widget = forms.PasswordInput,
        max_length = 30,
        required = True,
        label = 'New Password (again)',
    )

    class Meta:
        """
        Model metadata used to identify attributes in POST data when submitting
        a registration form. Required by users/views.py --> form =
        AccountCreateForm(request.Post). Throws error if removed.
        """
        def __init__(self):
            pass

        model = UserAccount
        fields = (
            'pass_old',
            'pass_new1',
            'pass_new2',
        )

    def clean(self):
        """
        clean cleans the data before comparing them and inserting into the
        database. Sends exception errors if tests are not passed.
        """
        pass_new1 = self.cleaned_data.get('pass_new1')
        pass_new2 = self.cleaned_data.get('pass_new2')

        if pass_new1 and pass_new2 and pass_new1 != pass_new2:
            raise forms.ValidationError("Passwords do not match.")

        return self.cleaned_data

