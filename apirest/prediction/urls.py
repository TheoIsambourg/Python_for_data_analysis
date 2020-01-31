from django.conf.urls import url
from prediction import views

urlpatterns = [
    url(r'^activities/$', views.activity_list),
    url(r'^predict/$', views.predict)
]