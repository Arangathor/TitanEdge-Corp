from django.urls import path
from . import views


urlpatterns = [

    path('', views.eafit_comercio, name="Eafit_comercio"),

]

