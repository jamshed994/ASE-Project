
from django.views.generic import DetailView, UpdateView, CreateView, View
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from performer.forms import UserCreationForm, VenueUpdateForm, PerformerUpdateForm


User = get_user_model()


class DetailUser(DetailView):
    model = User
    print ("Details view")
    def get_object(self, queryset=None):
        print (self.request)
        return self.request.user


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class UpdatePerformer(UpdateView):
    model = User
    form_class = PerformerUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

class UpdateVenue(UpdateView):
    model = User
    form_class = VenueUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
