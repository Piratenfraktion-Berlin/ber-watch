from django.conf import settings
from django.conf.urls import patterns, url

from big_projects_watch.urls import urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )