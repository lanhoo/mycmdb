from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.hello),
    url(r'^json_post/$', views.Json_post.as_view()),
    url(r'^jsonpost/', views.jsonpost),
]
