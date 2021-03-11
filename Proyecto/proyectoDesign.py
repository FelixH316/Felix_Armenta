# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyectoDesign.ui'
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
        Form.resize(349, 473)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 230, 331, 91))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zipLE = QLineEdit(self.groupBox)
        self.zipLE.setObjectName(u"zipLE")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.zipLE.setFont(font1)

        self.horizontalLayout_2.addWidget(self.zipLE)

        self.zipbuscarB = QPushButton(self.groupBox)
        self.zipbuscarB.setObjectName(u"zipbuscarB")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.zipbuscarB.setFont(font2)

        self.horizontalLayout_2.addWidget(self.zipbuscarB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.zipenviarB = QPushButton(self.groupBox)
        self.zipenviarB.setObjectName(u"zipenviarB")
        self.zipenviarB.setFont(font2)

        self.verticalLayout_2.addWidget(self.zipenviarB)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 331, 56))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.groupBox_2.setFont(font3)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.direccionL = QLabel(self.groupBox_2)
        self.direccionL.setObjectName(u"direccionL")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.direccionL.setFont(font4)
        self.direccionL.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.direccionL)

        self.puertoCB = QComboBox(self.groupBox_2)
        self.puertoCB.addItem("")
        self.puertoCB.addItem("")
        self.puertoCB.addItem("")
        self.puertoCB.setObjectName(u"puertoCB")
        self.puertoCB.setFont(font4)

        self.horizontalLayout.addWidget(self.puertoCB)

        self.conectarB = QPushButton(self.groupBox_2)
        self.conectarB.setObjectName(u"conectarB")
        self.conectarB.setFont(font4)

        self.horizontalLayout.addWidget(self.conectarB)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 80, 331, 141))
        self.groupBox_3.setFont(font)
        self.asistenciaB = QPushButton(self.groupBox_3)
        self.asistenciaB.setObjectName(u"asistenciaB")
        self.asistenciaB.setGeometry(QRect(10, 108, 311, 23))
        self.asistenciaB.setFont(font2)
        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 241, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.contraLE = QLineEdit(self.horizontalLayoutWidget)
        self.contraLE.setObjectName(u"contraLE")
        self.contraLE.setFont(font1)

        self.horizontalLayout_3.addWidget(self.contraLE)

        self.mostrarB = QPushButton(self.groupBox_3)
        self.mostrarB.setObjectName(u"mostrarB")
        self.mostrarB.setGeometry(QRect(260, 80, 61, 24))
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 26, 311, 48))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombreLE = QLineEdit(self.widget)
        self.nombreLE.setObjectName(u"nombreLE")
        self.nombreLE.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombreLE)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.correoLE = QLineEdit(self.widget)
        self.correoLE.setObjectName(u"correoLE")
        self.correoLE.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.correoLE)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 330, 331, 121))
        self.groupBox_4.setFont(font)
        self.pantallaTE = QTextEdit(self.groupBox_4)
        self.pantallaTE.setObjectName(u"pantallaTE")
        self.pantallaTE.setGeometry(QRect(10, 20, 311, 91))
        self.pantallaTE.viewport().setProperty("cursor", QCursor(Qt.ForbiddenCursor))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Archivo", None))
        self.zipLE.setText("")
        self.zipbuscarB.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.zipenviarB.setText(QCoreApplication.translate("Form", u"Enviar Archivo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Configuraci\u00f3n del Servidor", None))
        self.direccionL.setText(QCoreApplication.translate("Form", u"Direcci\u00f3n", None))
        self.puertoCB.setItemText(0, QCoreApplication.translate("Form", u"Puerto", None))
        self.puertoCB.setItemText(1, QCoreApplication.translate("Form", u"9998", None))
        self.puertoCB.setItemText(2, QCoreApplication.translate("Form", u"9997", None))

        self.conectarB.setText(QCoreApplication.translate("Form", u"Conectar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Informaci\u00f3n del Estudiante", None))
        self.asistenciaB.setText(QCoreApplication.translate("Form", u"Enviar Asistencia", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.mostrarB.setText(QCoreApplication.translate("Form", u"Mostrar", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Servidor", None))
    # retranslateUi
