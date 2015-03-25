from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from simpleajs.core.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('simpleajs.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contatos/$', ContactList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getdata/$', 'get_data'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()