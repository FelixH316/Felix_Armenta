# DESCRIPTION:  Main de la Tarea 4 - Base de datos local de la clase Estudiante
#               Muestra un menu que puede: publicar los 5 objetos iniciales de prueba, mostrar,
#               agregar, editar y eliminar estudiantes de la base de datos, además salir del
#               ciclo infinito del menu.
#               La gestion de la base de datos se realiza a través de Mongo Engine.
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

from mongoengine import *
from datetime import *
from paqueteT4.StudentIOv2 import Estudiante


class estudiantes(Document):
    nombre = StringField(required=True, max_length=70)
    correo = StringField(required=True, max_length=70)
    contrasena = StringField(required=True, max_length=20)
    materias = ListField(required=True)
    noControl = IntField(required=True, min_value=15240000, max_value=20249999)
    fecha = DateField(default=datetime.now())


class studentMongoManager():

    def __init__(self):
        connect("IECA", host="localhost", port=27017)
        listaConteo = estudiantes.objects()
        if listaConteo:
            self.conteo = len(listaConteo)
        else:
            self.conteo = 0

    def guardarEstudiante(self, student):
        post = estudiantes(
            nombre=student.getNombre(),
            correo=student.getCorreo(),
            contrasena=student.getContra(),
            materias=student.getMaterias(),
            noControl=student.getNoControl(),
        )
        post.save()
        print(f"\tEstudiante {student.getNoControl()} guardado")
        self.conteo += 1

    def mostrarEstudiantes(self):
        # print("\n\tNo. CONTROL\tNOMBRE\tCORREO\t\t\t\t\t\tPASSWORD")
        listaDB = estudiantes.objects()
        j = 0
        while (j < len(listaDB)):
            subjects = listaDB[j].materias
            print(f"\tNumero de Control: {listaDB[j].noControl} ______________________________________________")
            print(f"\tNombre: {listaDB[j].nombre} - Correo: {listaDB[j].correo} - Contrasena: {listaDB[j].contrasena}")
            print(f"\tMateria 1: {subjects[0]} - Materia 2: {subjects[1]} - Materia 3: {subjects[2]}")
            print(" ")
            j+=1

    def agregarEstudiante(self):
        name = input("\tIngresa nombre: ")
        mail = input("\tIngresa correo: ")
        password = input("\tIngresa contrasena: ")
        sub1 = input("\tIngresa materia 1: ")
        sub2 = input("\tIngresa materia 2: ")
        sub3 = input("\tIngresa materia 3: ")
        subLista = [sub1, sub2, sub3]
        alumno = Estudiante(name, mail, password, subLista)
        alumno.updateNoControl(self.conteo)
        self.guardarEstudiante(alumno)

    def editarEstudiante(self):
        self.mostrarEstudiantes()
        seleccion = input("\tIngresa el No. de Control del estudiante a modificar: ")
        modificado = estudiantes.objects(noControl=int(seleccion))
        name = input("\tIngresa nombre: ")
        mail = input("\tIngresa correo: ")
        password = input("\tIngresa contrasena: ")
        sub1 = input("\tIngresa materia 1: ")
        sub2 = input("\tIngresa materia 2: ")
        sub3 = input("\tIngresa materia 3: ")
        subLista = [sub1, sub2, sub3]
        nc = input("\tIngresa numero de control: ")
        modificado.update(nombre=name, correo=mail, contrasena=password,
                          materias=subLista, noControl=int(nc))

    def eliminarEstudiante(self):
        self.mostrarEstudiantes()
        seleccion = input("\tIngresa el No. de Control del estudiante a eliminar: ")
        eliminado = estudiantes.objects(noControl=int(seleccion))
        eliminado.delete()

if __name__ == '__main__':
    correr = True
    admi = studentMongoManager()
    studentData = [
        ["John Locke", "farmentaa.pci@ieca.mx", "Hatch4", ["Historia", "Matematicas", "Geografia"]],
        ["Jack Shepard", "3armenta@gmail.com", "Oceanic815", ["Electronica", "Calculo", "Termodinamica"]],
        ["Sayid Jarra", "15240784@leon.tecnm.mx", "Aye16", ["English", "Metodos Numericos", "Alebra Lineal"]],
        ["Kate Austen", "IECA.Tres@cinvestav.mx", "Austen23", ["Protocolos", "Dinamica", "Calculo Vectorial"]],
        ["James Ford", "ve14893@innovaccion.mx", "Ford42", ["Control", "Robotica", "Ecuaciones Diferenciales"]],
    ]

    while correr:
        print("\n\tREGISTRO DE ESTUDIANTES")
        print("\t1. Publicar registro inicial")
        print("\t2. Mostrar estudiantes")
        print("\t3. Editar estudiante")
        print("\t4. Agregar estudiante")
        print("\t5. Eliminar estudiante")
        print("\t6. Salir del programa")
        ans = input("\tIngresa el numero de tu seleccion: ")

        if ans == '1':
            print("\n\tSUBIENDO A BASE DE DATOS...")
            studentList = []
            for i in range(5):
                objeto = Estudiante(*studentData[i])
                objeto.updateNoControl(i)
                studentList.append(objeto)
                admi.guardarEstudiante(studentList[i])
        elif ans == '2':
            print("\n\tMOSTRANDO ESTUDIANTES...")
            admi.mostrarEstudiantes()
        elif ans == '3':
            print("\n\tEDITANDO ESTUDIANTE...")
            admi.editarEstudiante()
        elif ans == '4':
            print("\n\tAGREGANDO ESTUDIANTE...")
            admi.agregarEstudiante()
        elif ans == '5':
            print("\n\tELIMINANDO ESTUDIANTE...")
            admi.eliminarEstudiante()
        elif ans == '6':
            correr = False
        else:
            print("\tOpcion no valida")
