class Auto:
    # ----- Atributos -----
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # ----- Métodos o funciones -----
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Ejemplo de uso:
mi_auto = Auto("Toyota", "Corolla")
mi_auto.mostrar_info()
# _init_ se ejecuta de manera automática al crear un objeto de la clase Auto.
# Coloca tus autos favoritos