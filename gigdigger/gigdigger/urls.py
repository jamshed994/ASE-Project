from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html'), name='privacy_page'),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms_page'),
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='landing'),
    url(r'^performer/', include('performer.urls')),
    #url(r'^venue/', include('venue.urls')),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
