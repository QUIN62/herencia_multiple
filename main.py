
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeaArea

director = Director()

director.set_nombre("Panchito")
director.set_apellido("Perez")
director.set_edad(45)

director.set_cargo("Director ejevcutivo")
director.set_rfc("PAPE6734")
director.set_sueldo(28000)

director.set_nombre_del_area("Finanzas")
director.set_nivel(8)
director.set_seccion("A")


director.set_ubicacion("Ciudad de México")
director.set_codigo(2454)

jefe_area = JefeaArea()

jefe_area.set_nombre("Luis")
jefe_area.set_apellido("Ramirez")
jefe_area.set_edad(32)

jefe_area.set_cargo("Jefe en finanzas")
jefe_area.set_rfc("LIRA3380")
jefe_area.set_sueldo(19000)

jefe_area.set_nombre_del_area("Finanzas")
jefe_area.set_nivel(4)
jefe_area.set_seccion("G")


jefe_area.set_ubicacion("Verzacruz")
jefe_area.set_codigo(2489)

gerente = Gerente()

gerente.set_nombre("Mauricio")
gerente.set_apellido("Rodriguez")
gerente.set_edad(25)

gerente.set_cargo("Mantenimiento")
gerente.set_rfc("MARO9816")
gerente.set_sueldo(12000)

gerente.set_nombre_del_area("Mantenimiento y reparación")
gerente.set_nivel(1)
gerente.set_seccion("D")


gerente.set_ubicacion("Hidalgo")
gerente.set_codigo(2412)

print("Información Empleados")
print("")
director.mostrar_informacion_empleado()
print("")
jefe_area.mostrar_informacion_empleado()
print("")
gerente.mostrar_informacion_empleado()
print("")

print("Información Areas")
print("")
director.mostrar_informacion_area()
print("")
jefe_area.mostrar_informacion_area()
print("")
gerente.mostrar_informacion_area()