from django.conf import settings
from django.conf.urls import include, patterns, url

from django.contrib import admin
admin.autodiscover()

from big_projects_watch.urls import urlpatterns

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )