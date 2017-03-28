from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from venuea.views import DetailUser, UpdateUser, CreateUser, LogoutUser


urlpatterns = [
    url(r'^$', login_required(RedirectView.as_view(url=reverse_lazy('venuea_detail'), permanent=False))),
    url(r'^create/$', CreateUser.as_view(), name='venuea_create'),
    url(r'^detail/$', login_required(DetailUser.as_view()), name='venuea_detail'),
    url(r'^update/$', login_required(UpdateUser.as_view()), name='venuea_update'),
    url(r'^logout/$', LogoutUser.as_view(), name='venuea_logout'),
    url(r'', include('django.contrib.auth.urls')),
]
