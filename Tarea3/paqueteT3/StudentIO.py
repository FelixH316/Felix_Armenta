# DESCRIPTION:  Modulo con la clase estudiante
#               Fuera de la clase hay funciones para:
#               Guardar, mostrar y modifcar estudiantes
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

import shelve

class estudiante:
    def __init__(self, nombre, correo, contra):
        self.nombre = nombre
        self.correo = correo
        self.contra = contra

def guardarEstudiante(estudiante, strIndex):
    with shelve.open("students.db") as shelveFile:
        shelveFile[strIndex] = estudiante

def mostrarEstudiantes():
    print("\n\tNo.\tNOMBRE\tCORREO\t\t\t\t\t\tPASSWORD")
    with shelve.open("students.db") as shelveFile:
        for key in shelveFile:
            print (f"\t{int(key)+1}\t{shelveFile[key].nombre}\t{shelveFile[key].correo}\t\t{shelveFile[key].contra}")

def cambiarEstudiantes():
    mostrarEstudiantes()
    key = input("\tIngresa el indice del estudiante que desea modificar: ")
    key = int(key) - 1
    key = str(key)
    with shelve.open("students.db") as shelveFile:
        nNombre = input("\tIngresa el nuevo nombre: ")
        nCorreo = input("\tIngresa el nuevo correo: ")
        nContra = input("\tIngresa la nueva contra: ")
        nObjeto = estudiante(nNombre, nCorreo, nContra)
        shelveFile[key] = nObjeto

        # NOTA: De esta forma no funcionó la modificacion, pero no supe porque
        #shelveFile[key].nombre = input("\tIngresa el nuevo nombre: ")
        #shelveFile[key].correo = input("\tIngresa el nuevo correo: ")
        #shelveFile[key].contra = input("\tIngresa la nueva contra: ")
