from django.views.generic import ListView
from servicios.models import Servicio
from servicios.utils import ConfiguracionVisual

class ServiciosListView(ListView):
    model = Servicio
    template_name = "servicios/servicios.html"
    context_object_name = "servicios"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = ConfiguracionVisual()
        context["tema"] = config.obtener_tema()
        return context
