# DESCRIPTION:  Main de la Tarea 5 - Base de datos local para estudiantes
#               Genera una GUI que por medio de un QComboBox (menu desplegable) y un boton
#               selecciona la operacion.
#
#               Muestra un menu que puede: publicar los 5 objetos iniciales de prueba, mostrar,
#               agregar, editar y eliminar estudiantes de la base de datos.
#
#               La gestion de la base de datos se realiza a través de Mongo Engine.
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

from paqueteT5.studentIOv3 import Estudiante

import sys
from tarea5 import *
from mongoHandler import studentMongoManagerUI
from mongoHandler import estudiantes
from datetime import *


class Interfaz(QMainWindow):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.admi = studentMongoManagerUI()
        self.estadoRegistro(False)
        self.estadoEdicion(False)
        self.estadoBaja(False)

        self.ui.pantallaTE.setPlaceholderText("Aqui se muestran datos de estudiantes")
        self.ui.edBusquedaLE.setPlaceholderText("No. control actual")
        self.ui.edNoConLE.setPlaceholderText("Nuevo no. control")
        self.ui.selectorCB.activated.connect(self.enableSelector)
        self.ui.selectorB.clicked.connect(self.exeSelection)

        self.ui.actualizarB.clicked.connect(self.editarEstudiante)
        self.ui.edBusquedaLE.textEdited.connect(self.habEdicion)
        self.ui.edNoConLE.textEdited.connect(self.habEdicion)
        self.ui.edNombreLE.textEdited.connect(self.habEdicion)
        self.ui.edCorreoLE.textEdited.connect(self.habEdicion)
        self.ui.edContraLE.textEdited.connect(self.habEdicion)
        self.ui.edMat1LE.textEdited.connect(self.habEdicion)
        self.ui.edMat2LE.textEdited.connect(self.habEdicion)
        self.ui.edMat3LE.textEdited.connect(self.habEdicion)

        self.ui.registrarB.clicked.connect(self.agregarEstudiante)
        self.ui.regNombreLE.textEdited.connect(self.habRegistro)
        self.ui.regCorreoLE.textEdited.connect(self.habRegistro)
        self.ui.regContraLE.textEdited.connect(self.habRegistro)
        self.ui.regMat1LE.textEdited.connect(self.habRegistro)
        self.ui.regMat1LE.textEdited.connect(self.habRegistro)
        self.ui.regMat2LE.textEdited.connect(self.habRegistro)
        self.ui.regMat3LE.textEdited.connect(self.habRegistro)

        self.ui.borrarB.clicked.connect(self.eliminarEstudiante)
        self.ui.boNoConLE.textEdited.connect(self.habBaja)

    def enableSelector(self):
        estado = self.ui.selectorCB.currentIndex()
        if estado > 0:
            self.ui.selectorB.setEnabled(True)
        else:
            self.ui.selectorB.setDisabled(True)

    def showInfo(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Notificacion")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Information)
        # QMessageBox.Critical
        # QMessageBox.Warning
        msg.exec_()

    def mostrarEstudiantes(self):
        self.ui.pantallaTE.clear()
        listaDB = estudiantes.objects()
        if listaDB:
            j = 0
            while (j < len(listaDB)):
                subjects = listaDB[j].materias
                self.ui.pantallaTE.insertPlainText(f"Numero de Control: {listaDB[j].noControl} ______")
                self.ui.pantallaTE.insertPlainText(f"\nNombre: {listaDB[j].nombre} - Correo: {listaDB[j].correo} - Contrasena: {listaDB[j].contrasena}")
                self.ui.pantallaTE.insertPlainText(f"\nMateria 1: {subjects[0]} - Materia 2: {subjects[1]} - Materia 3: {subjects[2]}")
                self.ui.pantallaTE.insertPlainText("\n\n")
                j+=1
        else:
            self.showInfo("No hay estudiantes en la base de datos")

    def habBaja(self):
        tNC = len(self.ui.boNoConLE.text())
        if tNC > 7:
            self.ui.borrarB.setEnabled(True)
        else:
            self.ui.borrarB.setDisabled(True)

    def eliminarEstudiante(self):
        nc = self.ui.boNoConLE.text()
        eliminado = estudiantes.objects(noControl=int(nc))
        if eliminado:
            self.showInfo(f"Estudiante {eliminado[0].noControl} eliminado")
            eliminado[0].delete()
            self.mostrarEstudiantes()
        else:
            self.showInfo(f"No se encontro estudiante {int(nc)}")

    def habEdicion(self):
        toldNC = len(self.ui.edBusquedaLE.text())
        tnewNC = len(self.ui.edNoConLE.text())
        tname = len(self.ui.edNombreLE.text())
        tmail = len(self.ui.edCorreoLE.text())
        tpassword = len(self.ui.edCorreoLE.text())
        tsub1 = len(self.ui.edMat1LE.text())
        tsub2 = len(self.ui.edMat2LE.text())
        tsub3 = len(self.ui.edMat3LE.text())
        if (tname > 2) and (tmail > 5) and (tpassword > 3) and (tsub1 > 3) and (tsub2 > 3) and (tsub3 > 3) and (toldNC > 7) and (tnewNC > 7):
            self.ui.actualizarB.setEnabled(True)
        else:
            self.ui.actualizarB.setDisabled(True)

    def habRegistro(self):
        tname = len(self.ui.regNombreLE.text())
        tmail = len(self.ui.regCorreoLE.text())
        tpassword = len(self.ui.regContraLE.text())
        tsub1 = len(self.ui.regMat1LE.text())
        tsub2 = len(self.ui.regMat2LE.text())
        tsub3 = len(self.ui.regMat3LE.text())
        if (tname > 2) and (tmail > 5) and (tpassword > 3) and (tsub1 > 3) and (tsub2 > 3) and (tsub3 > 3):
            self.ui.registrarB.setEnabled(True)
        else:
            self.ui.registrarB.setDisabled(True)

    def agregarEstudiante(self):
        name = self.ui.regNombreLE.text()
        mail = self.ui.regCorreoLE.text()
        password = self.ui.regContraLE.text()
        sub1 = self.ui.regMat1LE.text()
        sub2 = self.ui.regMat2LE.text()
        sub3 = self.ui.regMat3LE.text()
        subLista = [sub1, sub2, sub3]
        alumno = Estudiante(name, mail, password, subLista)
        alumno.updateNoControl(self.admi.generarNoControl())
        self.admi.guardarEstudiante(alumno)
        self.showInfo(f"Estudiante {alumno.getNoControl()} guardado")
        self.mostrarEstudiantes()

    def editarEstudiante(self):
        oldNC = int(self.ui.edBusquedaLE.text())
        newNC = int(self.ui.edNoConLE.text())
        name = self.ui.edNombreLE.text()
        mail = self.ui.edCorreoLE.text()
        password = self.ui.edCorreoLE.text()
        sub1 = self.ui.edMat1LE.text()
        sub2 = self.ui.edMat2LE.text()
        sub3 = self.ui.edMat3LE.text()
        subLista = [sub1, sub2, sub3]
        if self.admi.validarNoCotrol(newNC, oldNC):
            self.showInfo("No. control actual o nuevo invalido")
        else:
            modificado = estudiantes.objects(noControl=oldNC)
            if modificado:
                modificado[0].update(nombre=name, correo=mail, contrasena=password,
                                     materias=subLista, noControl=newNC, fecha=datetime.now())
                self.showInfo("\nEstudiante editado")
                self.mostrarEstudiantes()
            else:
                self.showInfo("\nEstudiante no encotrado")


    def exeSelection(self):
        self.ui.pantallaTE.clear()
        estado = self.ui.selectorCB.currentIndex()
        if estado == 1:
            self.estadoRegistro(False)
            self.estadoEdicion(False)
            self.estadoBaja(False)
            self.ui.pantallaTE.insertPlainText("SUBIENDO A BASE DE DATOS...")
            if estudiantes.objects():
                self.showInfo("La base de datos ya tiene objetos")
            else:
                studentList = []
                for i in range(5):
                    objeto = Estudiante(*self.admi.studentData[i])
                    objeto.updateNoControl(self.admi.generarNoControl())
                    studentList.append(objeto)
                    self.admi.guardarEstudiante(studentList[i])
                self.showInfo("Registro inicial de estudiantes subido")
        elif estado == 2:
            self.mostrarEstudiantes()
            self.estadoRegistro(False)
            self.estadoEdicion(False)
            self.estadoBaja(False)
        elif estado == 3:
            self.showInfo("Ingrese los datos en el campo de edición")
            self.mostrarEstudiantes()
            self.estadoEdicion(True)
            self.estadoRegistro(False)
            self.estadoBaja(False)
        elif estado == 4:
            self.showInfo("Ingrese los datos en el campo de registro")
            self.mostrarEstudiantes()
            self.estadoRegistro(True)
            self.estadoEdicion(False)
            self.estadoBaja(False)
        elif estado == 5:
            self.mostrarEstudiantes()
            self.showInfo("Ingrese los datos en el campo de baja")
            self.estadoBaja(True)
            self.estadoRegistro(False)
            self.estadoEdicion(False)

    def estadoRegistro(self, estado):
        if estado is False:
            self.ui.registrarB.setEnabled(estado)
        self.ui.regNombreLE.setEnabled(estado)
        self.ui.regCorreoLE.setEnabled(estado)
        self.ui.regContraLE.setEnabled(estado)
        self.ui.regMat1LE.setEnabled(estado)
        self.ui.regMat1LE.setEnabled(estado)
        self.ui.regMat2LE.setEnabled(estado)
        self.ui.regMat3LE.setEnabled(estado)

    def estadoEdicion(self, estado):
        if estado is False:
            self.ui.actualizarB.setEnabled(estado)
        self.ui.edBusquedaLE.setEnabled(estado)
        self.ui.edNoConLE.setEnabled(estado)
        self.ui.edNombreLE.setEnabled(estado)
        self.ui.edCorreoLE.setEnabled(estado)
        self.ui.edContraLE.setEnabled(estado)
        self.ui.edMat1LE.setEnabled(estado)
        self.ui.edMat2LE.setEnabled(estado)
        self.ui.edMat3LE.setEnabled(estado)

    def estadoBaja(self, estado):
        if estado is False:
            self.ui.borrarB.setEnabled(estado)
        self.ui.boNoConLE.setEnabled(estado)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Interfaz()
    window.show()
    sys.exit(app.exec_())


    # while correr:
    #     print("\n\tREGISTRO DE ESTUDIANTES")
    #     print("\t1. Publicar registro inicial")
    #     print("\t2. Mostrar estudiantes")
    #     print("\t3. Editar estudiante")
    #     print("\t4. Agregar estudiante")
    #     print("\t5. Eliminar estudiante")
    #     print("\t6. Salir del programa")
    #     ans = input("\tIngresa el numero de tu seleccion: ")
    #
    #     if ans == '1':
    #         print("\n\tSUBIENDO A BASE DE DATOS...")
    #         if estudiantes.objects():
    #             print("\tWARNING: la base de datos ya tiene objetos")
    #
    #         else:
    #             studentList = []
    #             for i in range(5):
    #                 objeto = Estudiante(*studentData[i])
    #                 objeto.updateNoControl(admi.generarNoControl())
    #                 studentList.append(objeto)
    #                 admi.guardarEstudiante(studentList[i])
    #     elif ans == '2':
    #         print("\n\tMOSTRANDO ESTUDIANTES...")
    #         admi.mostrarEstudiantes()
    #     elif ans == '3':
    #         print("\n\tEDITANDO ESTUDIANTE...")
    #         admi.editarEstudiante()
    #     elif ans == '4':
    #         print("\n\tAGREGANDO ESTUDIANTE...")
    #         admi.agregarEstudiante()
    #     elif ans == '5':
    #         print("\n\tELIMINANDO ESTUDIANTE...")
    #         admi.eliminarEstudiante()
    #     elif ans == '6':
    #         correr = False
    #     else:
    #         print("\tOpcion no valida")
