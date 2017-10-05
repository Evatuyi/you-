from django.conf.urls import url
from . import views

from accounts.views import (login_view, auth_view, logout_view, invalid_view, loggedin_view)

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details_view),
    url(r'^add', views.add_view, name='add'),
    url(r'^location_list/$', views.location_list_view),
    

    # user auth urls
    url(r'^login/$', login_view),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout_view),
    url(r'^loggedin/$', loggedin_view),
    url(r'^invalid/$', invalid_view),

]
