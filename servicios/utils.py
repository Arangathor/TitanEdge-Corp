# servicios/utils.py

class ConfiguracionVisual:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionVisual, cls).__new__(cls)
            cls._instancia.tema = "oscuro"
        return cls._instancia

    def obtener_tema(self):
        return self.tema

    def cambiar_tema(self, nuevo_tema):
        self.tema = nuevo_tema
