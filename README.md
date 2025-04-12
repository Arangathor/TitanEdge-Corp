# Actividad 1 – Repositorio GitHub del Taller 01

Para esta actividad creamos un nuevo repositorio en GitHub exclusivamente para el Taller 01, con el fin de evitar alterar la versión original del proyecto U-Market desarrollado en Proyecto Integrador 1.

- **Repositorio creado:**  
  [https://github.com/<tu-usuario>/taller01-umarket](https://github.com/<tu-usuario>/taller01-umarket) *(Ejemplo, reemplazar con el tuyo)*

- **Objetivo del repositorio:**  
  Documentar e implementar los patrones de diseño y mejoras en arquitectura requeridas para el Taller 01, conservando el diseño original del sistema pero aplicando refactorizaciones y patrones.

- **Estructura mantenida:**  
  - Mismo nombre de apps (`servicios`, `carro`, `autenticacion`, etc.)
  - Base de datos SQLite local
  - URLs originales respetadas
  - Funcionalidades ya operativas: home, servicios, negociar, tienda, carrito, contacto, login/register


# Actividad 2 – Revisión Autocrítica del Proyecto

Durante el análisis del proyecto actual, identificamos lo siguiente con respecto a los parámetros de calidad vistos en clase:

## ✔️ Usabilidad

- ✅ Navegación sencilla con menú principal bien distribuido (Inicio, Servicios, Negociar, Tienda, Contacto, etc.)
- ✅ Formularios de login y registro accesibles
- ❌ **Mejorable:** feedback visual tras login exitoso/fallido podría ser más claro
- 🔧 **Inversión propuesta:** mejoras en la interfaz de carrito y en confirmación de contacto

## ✔️ Compatibilidad

- ✅ Funciona correctamente en navegadores modernos (Chrome, Firefox, Edge)
- ❌ **Mejorable:** aún no es completamente responsiva en móvil (algunos bloques se desajustan)
- 🔧 **Inversión propuesta:** adaptar Bootstrap o usar Flexbox para vistas de servicios y productos

## ✔️ Rendimiento

- ✅ Carga rápida gracias a la base de datos ligera SQLite
- ❌ **Mejorable:** las imágenes no están optimizadas (carga completa sin lazy-loading)
- 🔧 **Inversión propuesta:** usar compresión y `loading="lazy"` en tags `<img>`

## ✔️ Seguridad

- ✅ Manejo básico de autenticación implementado (login/register funcional)
- ❌ **Mejorable:** formularios sin protección contra CSRF, ni validación robusta
- 🔧 **Inversión propuesta:** usar validaciones backend en contacto y login + `@login_required` en rutas privadas

---

## 💸 Posibles puntos de inversión

- **Mejora en experiencia de usuario móvil**
- **Optimización del rendimiento con compresión de imágenes**
- **Sistema de roles y permisos más granular (cliente vs vendedor vs admin)**


# Actividades 3 a 5 – Taller 01 Proyecto Django (U-Market)

---

## ✅ Actividad 3 – Aplicación de un Patrón de Diseño Python

### 🎯 Patrón aplicado: Singleton

Creamos una clase Singleton en `utils.py` para centralizar la gestión del tema visual del sitio (oscuro/claro), evitando múltiples instancias de configuración.

### 📁 `servicios/utils.py`

```python
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
```

### 📁 `servicios/views.py` actualizado

```python
from servicios.utils import ConfiguracionVisual

def servicios(request):
    config = ConfiguracionVisual()
    tema_actual = config.obtener_tema()
    servicios = ServicioService.obtener_todos()
    return render(request, "servicios/servicios.html", {
        "servicios": servicios,
        "tema": tema_actual
    })
```

### 📄 `servicios.html` – Visualización del tema

```django
<section class="page-section clearfix">
  <div class="container">
    <div class="text-center p-4"
         style="background-color: #013220; color: white; border-radius: 15px;">
      <h2 class="section-heading mb-4">
        <span class="section-heading-upper" style="color: #90ee90;">CONFIGURACIÓN VISUAL</span><br>
        <span class="section-heading-lower" style="font-size: 1.8em;">TEMA ACTUAL: {{ tema|upper }}</span>
      </h2>
    </div>
  </div>
</section>
```

---

## ✅ Actividad 4 – Refactorización de la lógica en capas (services.py)

Creamos un archivo `services.py` para desacoplar la lógica del modelo desde las vistas, facilitando su reutilización y mantenimiento.

### 📁 `servicios/services.py`

```python
from servicios.models import Servicio

class ServicioService:
    @staticmethod
    def obtener_todos():
        return Servicio.objects.all()
```

### 📁 `views.py` usando capa de servicios

```python
from servicios.services import ServicioService

def servicios(request):
    config = ConfiguracionVisual()
    tema_actual = config.obtener_tema()
    servicios = ServicioService.obtener_todos()
    return render(request, "servicios/servicios.html", {
        "servicios": servicios,
        "tema": tema_actual
    })
```

---

## ✅ Actividad 5 – Aplicación de patrones Django (CBV + Normalización)

---

### Parte A – Uso de Vista Basada en Clase (`ListView`)

Reemplazamos la vista basada en función por una `ListView` para estructurar mejor la lógica y facilitar paginación, filtros, etc.

### 📁 `views.py`

```python
from django.views.generic import ListView

class ServiciosListView(ListView):
    model = Servicio
    template_name = "servicios/servicios.html"
    context_object_name = "servicios"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = ConfiguracionVisual()
        context["tema"] = config.obtener_tema()
        return context
```

### 📁 `urls.py`

```python
from .views import ServiciosListView

urlpatterns = [
    path('', ServiciosListView.as_view(), name="Servicios"),
]
```

---

### Parte B – Normalización del modelo `Servicio`

Se creó el modelo `CategoriaServicio` y se relacionó mediante `ForeignKey` con `Servicio`.

### 📁 `models.py`

```python
class CategoriaServicio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
```

### 📁 `admin.py`

```python
from .models import Servicio, CategoriaServicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("titulo", "categoria", "created")
    list_filter = ("categoria",)
    search_fields = ("titulo",)

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(CategoriaServicio)
```

### 📄 `servicios.html` – Mostrar la categoría

```django
{% if servicio.categoria %}
<span style="color: gray; font-size: 0.9em;">Categoría: {{ servicio.categoria.nombre }}</span>
{% else %}
<span style="color: gray; font-size: 0.9em;">Sin categoría</span>
{% endif %}
```

---

## ✅ Conclusión

- Se aplicaron tres patrones: **Singleton (Python), Service Layer, CBV y Normalización (Django)**
- El proyecto mantiene su funcionalidad original con mejoras escalables
- El código está listo para nuevas capas como roles, permisos y mejoras visuales
