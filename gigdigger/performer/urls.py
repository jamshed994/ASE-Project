from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from performer.views import DetailUser, UpdatePerformer, UpdateVenue, CreateUser, LogoutUser
from performer.views import ViewListingAll, LikeListing, ViewListingAll, CreateNewListing
from performer.views import RecordMyListing, ViewMyListing, FinalMyListing, ProfilePage, ViewEventsAll


urlpatterns = [
    url(r'^$', login_required(RedirectView.as_view(url=reverse_lazy('performer_detail'), permanent=False))),
    #url(r'^create/$', CreateUser.as_view(), name='performer_create'),
    url(r'^detail/$', login_required(DetailUser.as_view()), name='performer_detail'),
    url(r'^update_p/$', login_required(UpdatePerformer.as_view()), name='performer_update'),
    url(r'^update_v/$', login_required(UpdateVenue.as_view()), name='venue_update'),
    url(r'^logout/$', LogoutUser.as_view(), name='performer_logout'),
    url(r'^performer_signup/$', CreateUser.as_view(template_name='performer/performer_signup.html'), name = 'performer_signup'),
    url(r'^venue_signup/$', CreateUser.as_view(template_name='performer/venue_signup.html'), name = 'venue_signup'),
    url(r'^listing_success/$', RedirectView.as_view(url='/performer/detail'), name = 'listing_success'),
    url(r'^listing/create$', CreateNewListing , name='listing_new'),
    url(r'^listing/all$', ViewListingAll , name='listing_all'),
    url(r'^events/all$', ViewEventsAll , name='event_all'),
    url(r'^listing/mylisting$', ViewMyListing , name='my_listing'),
    url(r'^profile/(?P<username>\w+)/$', ProfilePage, name="performer_profile"),
    #url(r'^listing/select$', ViewListingSelect , name='listing_select'),
    url(r'^listing/listing_like/(?P<listing_id>\w+)/$', LikeListing, name="listing_like"),
    url(r'^listing/listing_like/(?P<listing_id>\w+)/success$', RedirectView.as_view(url='/detail')),
    url(r'^listing/listing_my/(?P<listing_id>\w+)/$', FinalMyListing, name="listing_final"),
    url(r'^listing/listing_my/(?P<listing_id>\w+)/(?P<username>\w+)/$', RecordMyListing, name="listing_record"),
    url(r'', include('django.contrib.auth.urls')),
]
