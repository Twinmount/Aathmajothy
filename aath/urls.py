from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("familythera",views.familythera,name="familythera"),
    path("childguide",views.childguide,name="childguide"),
    path("anxiety",views.anxiety,name="anxiety"),
    path("phobia",views.phobia,name="phobia"),
    path("depression",views.depression,name="depression"),
    path("couple",views.couple,name="couple"),
    path("marriage",views.marriage,name="marriage"),
    path("individual",views.individual,name="individual"),


]
