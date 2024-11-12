from classEmpleado import Empleado
from classArea import Area

class Gerente(Empleado,Area):
    def __init__(self):
        Empleado.__init__(self)
        Area.__init__(self)
        self._sucursal = ""

    # Getter y Setter
    def get_sucursal(self):
        return self._sucursal

    def set_sucursal(self, sucursal):
        self._sucursal = sucursal
