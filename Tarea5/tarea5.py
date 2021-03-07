# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tarea5.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(484, 588)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 50, 221, 221))
        self.registrarB = QPushButton(self.groupBox)
        self.registrarB.setObjectName(u"registrarB")
        self.registrarB.setGeometry(QRect(70, 190, 75, 23))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 201, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.regNombreL = QLabel(self.formLayoutWidget)
        self.regNombreL.setObjectName(u"regNombreL")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.regNombreL)

        self.regNombreLE = QLineEdit(self.formLayoutWidget)
        self.regNombreLE.setObjectName(u"regNombreLE")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.regNombreLE)

        self.regCorreoLE = QLineEdit(self.formLayoutWidget)
        self.regCorreoLE.setObjectName(u"regCorreoLE")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.regCorreoLE)

        self.regContraLE = QLineEdit(self.formLayoutWidget)
        self.regContraLE.setObjectName(u"regContraLE")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.regContraLE)

        self.regCorreoL = QLabel(self.formLayoutWidget)
        self.regCorreoL.setObjectName(u"regCorreoL")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.regCorreoL)

        self.regContraL = QLabel(self.formLayoutWidget)
        self.regContraL.setObjectName(u"regContraL")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.regContraL)

        self.regMat1L = QLabel(self.formLayoutWidget)
        self.regMat1L.setObjectName(u"regMat1L")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.regMat1L)

        self.regMat2L = QLabel(self.formLayoutWidget)
        self.regMat2L.setObjectName(u"regMat2L")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.regMat2L)

        self.regMat3L = QLabel(self.formLayoutWidget)
        self.regMat3L.setObjectName(u"regMat3L")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.regMat3L)

        self.regMat1LE = QLineEdit(self.formLayoutWidget)
        self.regMat1LE.setObjectName(u"regMat1LE")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.regMat1LE)

        self.regMat2LE = QLineEdit(self.formLayoutWidget)
        self.regMat2LE.setObjectName(u"regMat2LE")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.regMat2LE)

        self.regMat3LE = QLineEdit(self.formLayoutWidget)
        self.regMat3LE.setObjectName(u"regMat3LE")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.regMat3LE)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 50, 221, 271))
        self.actualizarB = QPushButton(self.groupBox_2)
        self.actualizarB.setObjectName(u"actualizarB")
        self.actualizarB.setGeometry(QRect(70, 240, 75, 23))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 201, 204))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edNoConL = QLabel(self.formLayoutWidget_2)
        self.edNoConL.setObjectName(u"edNoConL")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.edNoConL)

        self.edNoConLE = QLineEdit(self.formLayoutWidget_2)
        self.edNoConLE.setObjectName(u"edNoConLE")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.edNoConLE)

        self.edNombreL = QLabel(self.formLayoutWidget_2)
        self.edNombreL.setObjectName(u"edNombreL")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.edNombreL)

        self.edNombreLE = QLineEdit(self.formLayoutWidget_2)
        self.edNombreLE.setObjectName(u"edNombreLE")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.edNombreLE)

        self.edCorreoL = QLabel(self.formLayoutWidget_2)
        self.edCorreoL.setObjectName(u"edCorreoL")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.edCorreoL)

        self.edCorreoLE = QLineEdit(self.formLayoutWidget_2)
        self.edCorreoLE.setObjectName(u"edCorreoLE")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.edCorreoLE)

        self.edContraL = QLabel(self.formLayoutWidget_2)
        self.edContraL.setObjectName(u"edContraL")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.edContraL)

        self.edContraLE = QLineEdit(self.formLayoutWidget_2)
        self.edContraLE.setObjectName(u"edContraLE")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.edContraLE)

        self.edMat1L = QLabel(self.formLayoutWidget_2)
        self.edMat1L.setObjectName(u"edMat1L")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.edMat1L)

        self.edMat1LE = QLineEdit(self.formLayoutWidget_2)
        self.edMat1LE.setObjectName(u"edMat1LE")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.edMat1LE)

        self.edMat2L = QLabel(self.formLayoutWidget_2)
        self.edMat2L.setObjectName(u"edMat2L")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.edMat2L)

        self.edMat2LE = QLineEdit(self.formLayoutWidget_2)
        self.edMat2LE.setObjectName(u"edMat2LE")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.edMat2LE)

        self.edMat3L = QLabel(self.formLayoutWidget_2)
        self.edMat3L.setObjectName(u"edMat3L")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.edMat3L)

        self.edMat3LE = QLineEdit(self.formLayoutWidget_2)
        self.edMat3LE.setObjectName(u"edMat3LE")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.edMat3LE)

        self.edBusquedaL = QLabel(self.formLayoutWidget_2)
        self.edBusquedaL.setObjectName(u"edBusquedaL")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.edBusquedaL)

        self.edBusquedaLE = QLineEdit(self.formLayoutWidget_2)
        self.edBusquedaLE.setObjectName(u"edBusquedaLE")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.edBusquedaLE)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 380, 461, 201))
        self.pantallaTE = QTextEdit(self.groupBox_3)
        self.pantallaTE.setObjectName(u"pantallaTE")
        self.pantallaTE.setGeometry(QRect(10, 20, 441, 161))
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 280, 221, 91))
        self.formLayoutWidget_3 = QWidget(self.groupBox_4)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 20, 201, 31))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.boNoConL = QLabel(self.formLayoutWidget_3)
        self.boNoConL.setObjectName(u"boNoConL")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.boNoConL)

        self.boNoConLE = QLineEdit(self.formLayoutWidget_3)
        self.boNoConLE.setObjectName(u"boNoConLE")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.boNoConLE)

        self.borrarB = QPushButton(self.groupBox_4)
        self.borrarB.setObjectName(u"borrarB")
        self.borrarB.setGeometry(QRect(70, 60, 75, 23))
        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 0, 451, 51))
        self.selectorB = QPushButton(self.groupBox_5)
        self.selectorB.setObjectName(u"selectorB")
        self.selectorB.setGeometry(QRect(360, 20, 91, 23))
        self.selectorCB = QComboBox(self.groupBox_5)
        self.selectorCB.addItem("")
        self.selectorCB.addItem("")
        self.selectorCB.addItem("")
        self.selectorCB.addItem("")
        self.selectorCB.addItem("")
        self.selectorCB.addItem("")
        self.selectorCB.setObjectName(u"selectorCB")
        self.selectorCB.setGeometry(QRect(10, 20, 341, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"REGISTRO", None))
        self.registrarB.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.regNombreL.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.regCorreoL.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.regContraL.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.regMat1L.setText(QCoreApplication.translate("Form", u"Materia 1", None))
        self.regMat2L.setText(QCoreApplication.translate("Form", u"Materia 2", None))
        self.regMat3L.setText(QCoreApplication.translate("Form", u"Materia 3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"EDICION", None))
        self.actualizarB.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.edNoConL.setText(QCoreApplication.translate("Form", u"No Control", None))
        self.edNombreL.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.edCorreoL.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.edContraL.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.edMat1L.setText(QCoreApplication.translate("Form", u"Materia 1", None))
        self.edMat2L.setText(QCoreApplication.translate("Form", u"Materia 2", None))
        self.edMat3L.setText(QCoreApplication.translate("Form", u"Materia 3", None))
        self.edBusquedaL.setText(QCoreApplication.translate("Form", u"Busqueda", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"MOSTRAR", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"BAJA", None))
        self.boNoConL.setText(QCoreApplication.translate("Form", u"No Control", None))
        self.borrarB.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"SELECTOR", None))
        self.selectorB.setText(QCoreApplication.translate("Form", u"Seleccionar", None))
        self.selectorCB.setItemText(0, QCoreApplication.translate("Form", u"Selecciona una opcion", None))
        self.selectorCB.setItemText(1, QCoreApplication.translate("Form", u"Publicar registro inicial", None))
        self.selectorCB.setItemText(2, QCoreApplication.translate("Form", u"Mostrar estudiantes", None))
        self.selectorCB.setItemText(3, QCoreApplication.translate("Form", u"Editar estudiante", None))
        self.selectorCB.setItemText(4, QCoreApplication.translate("Form", u"Registrar estudiante", None))
        self.selectorCB.setItemText(5, QCoreApplication.translate("Form", u"Eliminar estudiante", None))

    # retranslateUi

