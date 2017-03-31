# coding=utf-8
from django import forms

from django.utils.translation import ugettext as _

from performer.models import User, Listing
import datetime


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'type_pv')

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


class PerformerUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'youtube1','y1d', 'youtube2', 'y2d', 'youtube3', 'y3d', 'soundcloud1','s1d','soundcloud2','s2d','soundcloud3','s3d','location', 'birthday', 'bio', 'gender', 'status')



class VenueUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'photo', 'location', 'bio', 'status', 'capacity', 'description', 'address', 'venue_name')


class ListingCreateForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    contact = forms.EmailField()
    ldatetime = forms.DateTimeField(initial=datetime.datetime.today)
    listing_id = forms.CharField(max_length=30)
    #listing_venue = forms.CharField(max_length=30)
    print ('Starting Form1')
    class Meta:
        model = Listing
        fields = ('subject', 'message', 'contact' , 'ldatetime' , 'listing_id' )




