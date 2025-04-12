from servicios.models import Servicio

class ServicioService:
    @staticmethod
    def obtener_todos():
        #print("Obteniendo servicios desde ServicioService...")
        return Servicio.objects.all()
