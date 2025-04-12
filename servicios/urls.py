from django.urls import path
from .views import ServiciosListView

urlpatterns = [
    path('', ServiciosListView.as_view(), name="Servicios"),
]
