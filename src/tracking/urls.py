from django.urls import path

from .views import home, refresh_elastic

urlpatterns = [
    path('', home, name='home'),
    path('refresh_elastic', refresh_elastic, name='refresh_elastic'),


]
