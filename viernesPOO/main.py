from cosas import *

def main():

    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("----- Herencia Alumno------")
    al1 = Alumno("Jose", 19, "234456", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("---------PROFESOR HERENCIA -------")
    profe1 = Profesor("Jesus", 30+16, "363565", "ING Software")
    print(profe1)
    profe1.dormir()

    print("---- Herencia Profe-----")
    ayudante = AyudanteProfesor("Adrian", 20, "5468556", "ICO", 232323, "ING software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")

main()