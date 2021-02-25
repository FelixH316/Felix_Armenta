# DESCRIPTION:  Main de la Tarea 3 - Serializacion de la clase estudiante con Shelve
#               Muestra un menu, permite mostrar y editar a los 5 objetos de la clase estudiante
#               Actualizando solo al archivo de datos ".dat" y respentando al directorio
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

from paqueteT3.StudentIO import estudiante
from paqueteT3.StudentIO import guardarEstudiante
from paqueteT3.StudentIO import mostrarEstudiantes
from paqueteT3.StudentIO import cambiarEstudiantes

if __name__ == '__main__':
    correr = True

    # NOTA: Este codigo lo use para ver las llaves de los datos del archivo .dat al inicar la ejecucion
    # with shelve.open("students.db") as shelveFile:
    #     klist = list(shelveFile.keys())
    #     print (klist)

    studentTuple = [
        ("John", "farmentaa.pci@ieca.mx", "Hatch4"),
        ("Jack", "3fel_armenta@gmail.com", "Oceanic815"),
        ("Sayid", "15240784@leon.tecnm.mx", "aye16"),
        ("Kate", "IECA.Tres@cinvestav.mx", "Austen23"),
        ("James", "ve14893@innovaccion.mx", "Ford42"),
    ]

    for i in range(5):
        objeto = estudiante(*studentTuple[i])  # El * indica que cada elemento de la tupla se va a pasar separado
        guardarEstudiante(objeto, str(i))      # es decir no se va a pasar la tupla como agrupacion

    #for info in studentTuple:
    #    e = estudiante(*info)   # El * indica que cada elemento de la tupla se va a pasar separado
    #    guardarEstudiante(e)    # es decir no se va a pasar la tupla como agrupacion

    while(correr):
        print("\n\tREGISTRO DE ESTUDIANTES")
        print("\t1. Mostrar estudiantes")
        print("\t2. Cambiar estudiantes")
        print("\t3. Salir del programa")
        ans = input("\tIngresa el numero de tu seleccion [X]: ")

        if (ans == '1'):
            # Limpiar pantalla
            mostrarEstudiantes()
        elif (ans == '2'):
            # Limpiar pantalla
            cambiarEstudiantes()
        elif (ans == '3'):
            correr = False
        else:
            print("\tOpcion no valida")
