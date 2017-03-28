from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from performer.views import DetailUser, UpdatePerformer, UpdateVenue, CreateUser, LogoutUser


urlpatterns = [
    url(r'^$', login_required(RedirectView.as_view(url=reverse_lazy('performer_detail'), permanent=False))),
    #url(r'^create/$', CreateUser.as_view(), name='performer_create'),
    url(r'^detail/$', login_required(DetailUser.as_view()), name='performer_detail'),
    url(r'^update_p/$', login_required(UpdatePerformer.as_view()), name='performer_update'),
    url(r'^update_v/$', login_required(UpdateVenue.as_view()), name='venue_update'),
    url(r'^logout/$', LogoutUser.as_view(), name='performer_logout'),
    url(r'^performer_signup/$', CreateUser.as_view(template_name='performer/performer_signup.html'), name = 'performer_signup'),
    url(r'^venue_signup/$', CreateUser.as_view(template_name='performer/venue_signup.html'), name = 'venue_signup'),
    url(r'', include('django.contrib.auth.urls')),
]
