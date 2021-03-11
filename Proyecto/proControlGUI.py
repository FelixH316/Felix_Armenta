# DESCRIPTION: Clase Gui, es la clase controladora de la GUI diseñada, incluye todos los
#               métodos/slots de control de la interfaz dependiendo de las signals registradas.
# AUTHOR: Félix Armenta Aguiñaga - IECA PADTS 3

from PySide2.QtWidgets import QFileDialog, QMessageBox, QLineEdit
from estudiante import Estudiante
from clienteChunks import Cliente
from proyectoDesign import *
import re


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pantallaTE.clear()
        self.ui.pantallaTE.setReadOnly(True)

        self.statusBar().showMessage("Incializando GUI...")
        self.clienteF = Cliente("3.16.226.150")

        self.ui.zipLE.setPlaceholderText("Ruta archivo .zip")
        self.ui.nombreLE.setPlaceholderText("Felix Armenta A")
        self.ui.correoLE.setPlaceholderText("3armenta@gmail.com")
        self.ui.contraLE.setPlaceholderText("PADTs_3?")

        self.ui.conectarB.setDisabled(True)
        self.ui.puertoCB.activated.connect(self.habConexion)
        self.ui.conectarB.clicked.connect(self.prepararConexion)

        self.ui.nombreLE.setDisabled(True)
        self.ui.correoLE.setDisabled(True)
        self.ui.contraLE.setDisabled(True)
        self.ui.mostrarB.setDisabled(True)
        self.ui.mostrarB.clicked.connect(self.mostrarContra)
        self.ui.contraLE.setEchoMode(QLineEdit.Password)
        self.ui.nombreLE.textEdited.connect(self.habAsistencia)
        self.ui.correoLE.textEdited.connect(self.habAsistencia)
        self.ui.contraLE.textEdited.connect(self.habAsistencia)
        self.ui.asistenciaB.setDisabled(True)
        self.ui.asistenciaB.clicked.connect(self.regAsistencia)

        self.ui.zipLE.setDisabled(True)
        self.ui.zipbuscarB.setDisabled(True)
        self.ui.zipenviarB.setDisabled(True)
        self.ui.zipbuscarB.clicked.connect(self.buscarArchivo)
        self.ui.zipLE.textChanged.connect(self.habEnvArchivo)
        self.ui.zipenviarB.clicked.connect(self.envArchivo)
        self.statusBar().showMessage("Selecciona un puerto...")


    def habConexion(self):
        self.statusBar().showMessage("Configurando conexión...")
        seleccion = self.ui.puertoCB.currentIndex()
        self.ui.pantallaTE.clear()
        if seleccion > 0:
            self.ui.conectarB.setEnabled(True)
            self.ui.direccionL.setText(self.clienteF.getIP())
        else:
            self.ui.conectarB.setDisabled(True)
            self.ui.direccionL.setText("Dirección")

    def prepararConexion(self):
        self.ui.puertoCB.setDisabled(True)
        self.ui.conectarB.setDisabled(True)

        self.ui.pantallaTE.setPlainText("Parametros de conexion establecidos\n")

        self.ui.nombreLE.setEnabled(True)
        self.ui.correoLE.setEnabled(True)
        self.ui.contraLE.setEnabled(True)
        self.ui.mostrarB.setEnabled(True)
        self.habAsistencia()

    def habAsistencia(self):
        self.statusBar().showMessage("Editando datos de asistencia...")
        tN = self.ui.nombreLE.text()
        tC = self.ui.correoLE.text()
        tP = self.ui.contraLE.text()
        vCorreo = self.validaCorreo(tC)
        vContra = self.validaContra(tP)

        if (tN == "Felix Armenta A") and vCorreo and vContra:
            self.ui.asistenciaB.setEnabled(True)
        else:
            self.ui.asistenciaB.setDisabled(True)

    def regAsistencia(self):
        self.ui.nombreLE.setDisabled(True)
        self.ui.correoLE.setDisabled(True)
        self.ui.contraLE.setDisabled(True)
        alumno = Estudiante(self.ui.nombreLE.text(), self.ui.correoLE.text(), self.ui.contraLE.text())
        self.mostrarAlerta("Conexión con el servidor establecida")
        self.clienteF = Cliente("3.16.226.150")
        self.clienteF.setPuerto(int(self.ui.puertoCB.currentText()))  # Retorna str, castear a int
        self.clienteF.conectar()
        self.ui.pantallaTE.clear()
        msj = self.clienteF.enviar(alumno)
        self.ui.pantallaTE.insertPlainText(msj + '\n')
        print(msj)
        self.statusBar().showMessage("Selecciona tu archivo...")
        self.ui.asistenciaB.setDisabled(True)
        self.ui.zipLE.setEnabled(True)
        self.ui.zipbuscarB.setEnabled(True)

    def buscarArchivo(self):
        filename, _ = QFileDialog.getOpenFileName(filter="*.zip")   # Retorna la ruta y el filtro
        self.ui.zipLE.setText(filename)

    def habEnvArchivo(self):
        ruta = len(self.ui.zipLE.text())
        if ruta > 9:
            self.ui.zipenviarB.setEnabled(True)
        else:
            self.ui.zipenviarB.setDisabled(True)

    def envArchivo(self):
        self.ui.zipLE.setDisabled(True)
        ruta = self.ui.zipLE.text()
        archivo = open(ruta, "rb")
        res = self.clienteF.enviar(archivo.read())
        self.ui.pantallaTE.insertPlainText(res)
        print(res)
        self.clienteF.desconectar()
        self.mostrarAlerta("Conexión con el servidor cerrada")
        self.ui.zipenviarB.setDisabled(True)
        self.ui.zipbuscarB.setDisabled(True)
        self.ui.puertoCB.setEnabled(True)
        self.ui.conectarB.setEnabled(True)
        self.statusBar().showMessage("Selecciona un puerto...")

    def mostrarAlerta(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Notificacion")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QMessageBox.Critical)
        # msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def mostrarContra(self):
        if self.ui.contraLE.echoMode() == QLineEdit.Password:
            self.ui.contraLE.setEchoMode(QLineEdit.Normal)
            self.ui.mostrarB.setText("Ocultar")
        else:
            self.ui.contraLE.setEchoMode(QLineEdit.Password)
            self.ui.mostrarB.setText("Mostrar")

    def validaCorreo(self, cadena):
        # \w caracter alfanumerico y '_' tambien
        patronCorreo = "[\w]{1,}\."
        patronCorreo1Nom = "^[\w]+@[\w]+\.[\w]+[\.]?[\w]*"
        patronCorreo2Nom = "\.[\w]+@[\w]+\.[\w]+[\.]?[\w]*"
        if (re.match(patronCorreo, cadena) is None):
            banderaCorreo = re.search(patronCorreo1Nom, cadena)
        else:
            banderaCorreo = re.search(patronCorreo2Nom, cadena)

        # print(banderaCorreo)

        if (banderaCorreo is None):
            # Formato de correo invalido
            return False
        else:
            # Formato de correo valido
            return True

    def validaContra(self, cadena):
        patronLower = "[a-z]+"
        patronUpper = "[A-Z]+"
        patronNum = "[0-9]+"
        patronSimb = "[\W_]+"
        tam = len(cadena)
        bLower = re.search(patronLower, cadena)
        bUpper = re.search(patronUpper, cadena)
        bNum = re.search(patronNum, cadena)
        bSimb = re.search(patronSimb, cadena)
        if (tam >= 8) and (bLower is not None) and (bUpper is not None) and \
                (bNum is not None) and (bSimb is not None):
            return True
        else:
            return False
