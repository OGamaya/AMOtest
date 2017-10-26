from django.conf.urls import url

from comun import views

urlpatterns = [
    url(r'^$', views.Home, name='index'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^isLogged/$', views.logged_view, name='isLogged'),
]
