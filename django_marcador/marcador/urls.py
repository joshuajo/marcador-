from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='marcador_bookmark_user'),
    url(r'^$', views.bookmark_list, name='marcador_bookmark_list'),
]
