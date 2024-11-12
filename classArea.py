
from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        Departamento.__init__(self)
        self._nivel = 0
        self._seccion = ""
        self._nombre_del_area = ""


    # Getter y Setter
    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel

    def get_seccion(self):
        return self._seccion
    def set_seccion(self, seccion):
        self._seccion = seccion
    def get_nombre_del_area(self):
        return self._nombre_del_area
    def set_nombre_del_area(self, nombre_del_area):
        self._nombre_del_area = nombre_del_area

    def mostrar_informacion_area(self):
        print(f"Nombre del area: {self._nombre_del_area}, Sección: {self._seccion}"
              f"Ubicacion del departamento: {self.get_ubicacion()}, Codigo: {self.get_codigo()}")