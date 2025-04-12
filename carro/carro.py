class Carro:

    def __init__(self, request):
        
        self.request = request
        self.session = request.session
        # Inicializa el carro en la sesión si no existe
        carro = self.session.get("carro", {})
        
        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro = carro
        


    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:  # Si el producto no está en el carro
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break            
        
        self.guardar_carro()



    def guardar_carro(self):
        # Actualiza la sesión con el estado actual del carro y marca como modificada
        self.session["carro"] = self.carro
        self.session.modified = True



    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]  # Elimina el producto del carro
            self.guardar_carro()



    def restar_producto(self, producto):
        for key, value in self.carro.items():
            #producto_id = str(producto.id)
            if key in str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.precio

                # Elimina el producto si la cantidad es menor a 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()


    def limpiar_carro(self):
        # Vacía el carro y marca la sesión como modificada
        self.session["carro"] = {}
        self.session.modified = True
