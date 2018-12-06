from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
     url(r'^$', views.post_list, name='post_list'),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]






