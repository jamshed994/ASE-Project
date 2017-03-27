
from django.views.generic import DetailView, UpdateView, CreateView, View
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from performer.forms import CustomUserCreationForm, VenueCreationForm, PerformerCreationForm, UserUpdateForm


User = get_user_model()


class DetailUser(DetailView):
    model = User
    print ("Details view")
    def get_object(self, queryset=None):
        print (self.request)
        return self.request.user


class CreateUser(CreateView):
    model = User
    form_class = CustomUserCreationForm

class CreatePerformer(CreateView):
    model = User
    form_class = PerformerCreationForm
    success_url = reverse_lazy( 'success')
    def register_account(request):
        template = 'auth/performer_signup.html'
        if request.POST:
            form = PerformerCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password1 = form.cleaned_data['password1']
                u = User(username=username, email=email, last_name=last_name, first_name=first_name)
                u.set_password(password1)
                u.save()

                return HttpResponseRedirect('auth/success.html')

        else:
            form = PerformerCreationForm()
        return render_to_response(template,
                              {'form': form}, context_instance=RequestContext(request))
    def register_success(request):
        print("Hello")
        return render_to_response(
            'auth/success.html',
            )


class CreateVenue(CreateView):
    model = User
    form_class = VenueCreationForm
    success_url = reverse_lazy( 'venue_success')
    def register_account(request):
        template = 'auth/venue_signup.html'
        if request.POST:
            form = VenueCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password1 = form.cleaned_data['password1']
                u = User(username=username, email=email, last_name=last_name, first_name=first_name)
                u.set_password(password1)
                u.save()

                return HttpResponseRedirect('auth/venue_success.html')
        else:
            form = VenueCreationForm()
        return render_to_response(template,
                              {'form': form}, context_instance=RequestContext(request))

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


 


class UpdateUser(UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
