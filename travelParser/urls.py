"""
travelParser URL Configuration
"""
from django.conf.urls import url, include
from travelParser import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Parse
    url(r'^parse/$', views.parse),
    # Auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
