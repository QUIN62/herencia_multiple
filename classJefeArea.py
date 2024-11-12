from classEmpleado import Empleado
from classArea import Area

class JefeaArea(Empleado,Area):
    def __init__(self):
        Empleado.__init__(self)
        Area.__init__(self)
        self._tienda = ""

    # Getter y Setter
    def get_tienda(self):
        return self._tienda

    def set_tienda(self, tienda):
        self._tienda = tienda

