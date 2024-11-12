from classEmpleado import Empleado
from classArea import Area

class Director(Empleado,Area):
    def __init__(self):
        Empleado.__init__(self)
        Area.__init__(self)
        self._region = ""

    # Getter y Setter
    def get_region(self):
        return self._region

    def set_region(self, region):
        self._region = region


def informacion_director(self):
    print(f"Nombre: {self.get_nombre()} {self.get_apellido()}")
