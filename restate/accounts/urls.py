from django.urls import path
from . import views


urlpatterns=[
    path('login',views.login,name='login'),
    path("register", views.register, name='register'),
    path("logout", views.logout, name='logout'),
    path("settings", views.settings, name='settings'),
    path("delete", views.delete, name='delete'),
    path("pchange", views.pchange, name='pchange'),

]