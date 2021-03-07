# DESCRIPTION: Archivo de clases
#              Incluye el modelo de publicacion a Mongo DB por Mongo Engine
#              Incluye clase que actua como administrado de publicacion
# AUTHOR: Félix Armenta Aguiñaga - IECA PADTS 3

from mongoengine import *
from datetime import *
from paqueteT5.studentIOv3 import Estudiante


class estudiantes(Document):
    nombre = StringField(required=True, max_length=70)
    correo = StringField(required=True, max_length=70)
    contrasena = StringField(required=True, max_length=50)
    materias = ListField(required=True)
    noControl = IntField(required=True, min_value=10240000, max_value=20249999)
    fecha = DateTimeField(default=datetime.now())


class studentMongoManagerUI:
    studentData = [
        ["John Locke", "farmentaa.pci@ieca.mx", "Hatch4", ["Historia", "Matematicas", "Geografia"]],
        ["Jack Shepard", "3armenta@gmail.com", "Oceanic815", ["Electronica", "Calculo", "Termodinamica"]],
        ["Sayid Jarra", "15240784@leon.tecnm.mx", "Aye16", ["English", "Metodos Numericos", "Alebra Lineal"]],
        ["Kate Austen", "IECA.Tres@cinvestav.mx", "Austen23", ["Protocolos", "Dinamica", "Calculo Vectorial"]],
        ["James Ford", "ve14893@innovaccion.mx", "Ford42", ["Control", "Robotica", "Ecuaciones Diferenciales"]],
    ]

    def __init__(self):
        connect("IECA", host="localhost", port=27017)
        self.conteo = len(estudiantes.objects())

    def generarNoControl(self):
        nc = self.conteo
        nc += 20240000
        while self.validarNoCotrol(nc):
            nc += 1
            self.conteo += 1
        return nc

    def validarNoCotrol(self, newNoControl, oldNoControl=None):
        if (newNoControl < 10240000) or (newNoControl > 20249999):
            print("\tNo de control no valido, rango de 10240000 a 20249999")
            return True
        lista = estudiantes.objects()
        if lista:
            if newNoControl == oldNoControl:
                return False
            for i in range(len(lista)):
                if newNoControl == lista[i].noControl:
                    return True
            return False
        else:
            return False

    def guardarEstudiante(self, student):
        post = estudiantes(
            nombre=student.getNombre(),
            correo=student.getCorreo(),
            contrasena=student.getContra(),
            materias=student.getMaterias(),
            noControl=student.getNoControl(),
            fecha=datetime.now()
        )
        post.save()
        print(f"\tEstudiante {student.getNoControl()} guardado")

    # def mostrarEstudiantes(self):
    #     listaDB = estudiantes.objects()
    #     if listaDB:
    #         j = 0
    #         while (j < len(listaDB)):
    #             subjects = listaDB[j].materias
    #             print(f"\tNumero de Control: {listaDB[j].noControl} ______________________________________________")
    #             print(f"\tNombre: {listaDB[j].nombre} - Correo: {listaDB[j].correo} - Contrasena: {listaDB[j].contrasena}")
    #             print(f"\tMateria 1: {subjects[0]} - Materia 2: {subjects[1]} - Materia 3: {subjects[2]}")
    #             print(" ")
    #             j+=1
    #     else:
    #         print("\t No hay estudiantes en la base de datos")

    def agregarEstudiante(self):
        name = input("\tIngresa nombre: ")
        mail = input("\tIngresa correo: ")
        password = input("\tIngresa contrasena: ")
        sub1 = input("\tIngresa materia 1: ")
        sub2 = input("\tIngresa materia 2: ")
        sub3 = input("\tIngresa materia 3: ")
        subLista = [sub1, sub2, sub3]
        alumno = Estudiante(name, mail, password, subLista)
        alumno.updateNoControl(self.generarNoControl())
        self.guardarEstudiante(alumno)

    # def editarEstudiante(self):
    #     self.mostrarEstudiantes()
    #     seleccion = input("\tIngresa el No. de Control del estudiante a modificar: ")
    #     modificado = estudiantes.objects(noControl=int(seleccion))
    #     # print(type(modificado)) # Modificado trae una lista de objetos
    #     name = input("\tIngresa nombre: ")
    #     mail = input("\tIngresa correo: ")
    #     password = input("\tIngresa contrasena: ")
    #     sub1 = input("\tIngresa materia 1: ")
    #     sub2 = input("\tIngresa materia 2: ")
    #     sub3 = input("\tIngresa materia 3: ")
    #     subLista = [sub1, sub2, sub3]
    #     nc = input("\tIngresa numero de control: ")
    #     while self.validarNoCotrol(int(nc), int(seleccion)):
    #         nc = input("\tWARNING repetido, ingresa numero de control: ")
    #     modificado[0].update(nombre=name, correo=mail, contrasena=password,
    #                          materias=subLista, noControl=int(nc), fecha=datetime.now())
    #     print(f"\tEstudiante {modificado[0].noControl} editado")


    # def eliminarEstudiante(self):
    #     self.mostrarEstudiantes()
    #     seleccion = input("\tIngresa el No. de Control del estudiante a eliminar: ")
    #     eliminado = estudiantes.objects(noControl=int(seleccion))
    #     if eliminado:
    #         print(f"\tEstudiante {eliminado[0].noControl} eliminado")
    #         eliminado[0].delete()
    #     else:
    #         print(f"\tWARNING: No se encontro estudiante {int(seleccion)}")