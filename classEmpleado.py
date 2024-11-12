
from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        Persona().__init__(self)
        self._cargo = ""
        self._sueldo = 0
        self._rfc = ""


    # Getter y Setter
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_rfc(self):
        return self._rfc

    def set_rfc(self, rfc):
        self._rfc = rfc

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def mostrar_informacion_empleado(self):
        print(f"Nombre: {self.get_nombre()}, Apellido: {self.get_apellido()}"
              f"Edad: {self.get_edad()}, Puesto: {self.get_cargo()}"
              f"RFC: {self.get_rfc()}, Sueldo: {self.get_sueldo()}")
