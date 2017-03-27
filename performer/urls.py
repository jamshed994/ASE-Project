from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from performer.views import DetailUser, UpdateUser, CreateUser, LogoutUser, CreatePerformer, CreateVenue


urlpatterns = [
	
    url(r'^$', login_required(RedirectView.as_view(url=reverse_lazy('performer_detail'), permanent=False))),
    #user login
    #url(r'^create/$', CreateUser.as_view(), name='performer_create'),
    url(r'^venue_success/$', CreateVenue.as_view(template_name='auth/venue_success.html'), name="venue_success"),
    url(r'^success/$', CreateVenue.as_view(template_name='auth/success.html'), name="success"),
    url(r'^detail/$', login_required(DetailUser.as_view()), name='performer_detail'),
    url(r'^update/$', login_required(UpdateUser.as_view()), name='performer_update'),
    url(r'^logout/$', LogoutUser.as_view(), name='performer_logout'),
    url(r'^performer_signup/$', CreatePerformer.as_view(template_name='auth/performer_signup.html'), name = 'performer_create'),
    url(r'^venue_signup/$', CreateVenue.as_view(template_name='auth/venue_signup.html'), name = 'venue_signup'),
    url(r'', include('django.contrib.auth.urls')),
    
]
