############
#URL : Regular Expression
############
from django.conf.urls import url
from django.contrib import admin
from .views import my_templates

urlpatterns = [
    url(r"^$", my_templates)
]
############
# URL : path
############
#from django.urls import path
#from . import views

#urlpatterns = [
#    path("", views.my_templates, name="my_templates")
#]