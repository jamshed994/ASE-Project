# coding=utf-8
from django import forms

from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from performer.models import User, Venue, Performer

class CustomUserCreationForm(UserCreationForm):
 
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
class VenueCreationForm(UserCreationForm):
    venue_id = forms.CharField(label="Venue Id", max_length=30, required=True,
                                  help_text="Required. 30 characters or fewer.")
 
    class Meta:
        model = Venue
        fields = ('username','email','first_name')

class PerformerCreationForm(UserCreationForm):
    performer_id = forms.CharField(label="Performer Id", max_length=30, required=True,
                                  help_text="Required. 30 characters or fewer.")
 
    class Meta:
        model = Performer
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'youtube', 'soundcloud', 'birthday', 'bio', 'gender', 'status')
'''
 class FacebookUserCreationForm(UserCreationForm):
    Facebook_id = forms.CharField(label="Facebook Id", max_length=30, required=True,
                                  help_text="Required. 30 characters or fewer.")
 
    class Meta:
        model = FacebookUser



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
'''

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
