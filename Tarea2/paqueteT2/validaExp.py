# DESCRIPTION:  Modulo para validacion de correos, telefonos, CURP y RFC
#               Vease el ejemplo dentro de if __name__ == '__main__':
#               para distinguir los formatos validos e invalidos.
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

import re

def validaCorreo(cadena):
    # \w caracter alfanumerico y '_' tambien
    patronCorreo = "[\w]{1,}\."
    patronCorreo1Nom = "^[\w]+@[\w]+\.[\w]+[\.]?[\w]*"
    patronCorreo2Nom = "\.[\w]+@[\w]+\.[\w]+[\.]?[\w]*"
    if (re.match(patronCorreo, cadena) is None):
        banderaCorreo = re.search(patronCorreo1Nom, cadena)
    else:
        banderaCorreo = re.search(patronCorreo2Nom, cadena)

    # print(banderaCorreo)

    if(banderaCorreo is None):
        # No es un formato de correo invalido
        return False
    else:
        # Es un formato de correo valido
        return True

def validaTel(cadena):
    patronesTel = ("\d{10}", "\(\d{3}\)\d{7}", "\(\d{2}\) \d{4} \d{4}", "\(\d{3}\) \d{3}-\d{4}")
    for i in patronesTel:
        if (re.match(i, cadena) is not None):
            return True
    else:
        return False

def validaRFC(cadena):
    patronRFC = "^[a-zA-Z]{4}[\d]{6}[a-zA-Z\d]{3}"
    banderaRFC = re.search(patronRFC, cadena)
    if (banderaRFC is None):
        return False
    else:
        return True

def validaCURP(cadena):
    # En la parte de la CURP [H|M] para que sea forzoso uno u otro
    patronCURP = "[a-zA-Z]{4}\d{6}[HMhm][a-zA-Z]{5}[a-zA-Z0-9]\d"
    banderaCURP = re.match(patronCURP, cadena)
    if (banderaCURP is None):
        return False
    else:
        patronFecha = "^([a-zA-Z]{4})(\d{2})(\d{2})(\d{2})"
        Fecha = re.search(patronFecha, cadena)
        year = int(Fecha.group(2))
        mes = int(Fecha.group(3))
        dia = int(Fecha.group(4))
        if ((mes > 12) or (dia > 31)):
            return False
        else:
            cadenaSexo = re.search("(\d{6})([a-zA-Z])", cadena)
            sexo = cadenaSexo.group(2)
            if((sexo == 'h') or (sexo == 'm') or (sexo == 'H') or (sexo == 'M')):
                estados = ("AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", "GT",
                           "GR", "HG", "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL", "QT",
                           "QR", "SP", "SL", "SR", "TC", "TS", "TL", "VZ", "YN", "ZC", "NE",
                           "as", "bc", "bs", "cc", "cl", "cm", "cs", "ch", "df", "dg", "gt",
                           "gr", "hg", "jc", "mc", "mn", "ms", "nt", "nl", "oc", "pl", "qt",
                           "qr", "sp", "sl", "sr", "tc", "ts", "tl", "vz", "yn", "zc", "ne")

                cadenaEstado = re.search("(\d{6}[a-zA-Z])([a-zA-Z]{2})", cadena)
                estado = cadenaEstado.group(2)
                for i in estados:
                    if(estado == i):
                        break
                else:
                    return False

                if (year < 22):
                    patronSiglo = "\d{6}[a-zA-Z]{6}[a-zA-Z]"
                    cadenaSiglo = re.search(patronSiglo, cadena)
                    if (cadenaSiglo is None):
                        return False
                    else:
                        return True
                else:
                    patronSiglo = "\d{6}[a-zA-Z]{6}[0-9]"
                    cadenaSiglo = re.search(patronSiglo, cadena)
                    if (cadenaSiglo is None):
                        return False
                    else:
                        return True
            else:
                return False

if __name__ == '__main__':
    correosCorrectos = ("juan.valenzuela@curso.python.mx",
                       "3armenta@gmail.com",
                       "15240784@leon.tecnm.mx",
                       "ve14893@innovaccion.mx",
                       "IECA.Tres@cinvestav.mx",
                       "scorch316@ieee.org")
    correosIncorrectos = ("juan.valenzuela_curso.python.mx",
                         "@gmail.com",
                         "15240784@leon",
                         "ve1489.@innovaccion.mx",
                         "IECA.Tres@")
    print("\nDEMO DE CORREOS VALIDOS")
    for i in correosCorrectos:
        if (validaCorreo(i)):
            print(f"El correo [{i}] es valido")
        else:
            print(f"El correo [{i}] es invalido")
    print("\nDEMO DE CORREOS INVALIDOS")
    for i in correosIncorrectos:
        if (validaCorreo(i)):
            print(f"El correo [{i}] es valido")
        else:
            print(f"El correo [{i}] es invalido")

    numCorrectos = ("4771744416",
                    "(081)8499485",
                    "(05) 5323 9077",
                    "(479) 123-4567")
    numIncorrectos = ("(33)12345678",
                      "492 765 2839",
                      "346-304-3094",
                      "AFAA930918"
                      )
    print("\nDEMO DE TELEFONOS VALIDOS")
    for i in numCorrectos:
        if (validaTel(i)):
            print(f"El telefono {i} es valido")
        else:
            print(f"El telefono {i} es invalido")
    print("\nDEMO DE TELEFONOS INVALIDOS")
    for i in numIncorrectos:
        if (validaTel(i)):
            print(f"El telefono {i} es valido")
        else:
            print(f"El telefono {i} es invalido")

    rfcCorrectos = ("AEAF970221KX9",
                    "MERA010701TY8",
                    "mAhC970513uQ9"
                    )
    rfcIncorrectos = ("AE_F970221KX9",
                      "8935389453TPM",
                      "a2t30406309V8",
                      "AFAA930918"
                      )
    print("\nDEMO DE RFC VALIDOS")
    for i in rfcCorrectos:
        if (validaRFC(i)):
            print(f"El RFC [{i}] es valido")
        else:
            print(f"El RFC [{i}] es invalido")
    print("\nDEMO DE RFC INVALIDOS")
    for i in rfcIncorrectos:
        if (validaRFC(i)):
            print(f"El RFC [{i}] es valido")
        else:
            print(f"El RFC [{i}] es invalido")

    curpCorrectas = ("AEAF970221HGTRGL04",
                     "EBDC040630MGTUZRX7",
                     "aeaf970221hgtrgl04",
                     "ebdc040630mgtuzrx7",
                     "MERA010701HGTNMNA9",
                     "mahc970513hgtrrs06"
                     )
    curpIncorrectas = ("A2T3040630MGTUZRX7",
                       "aetaATIAPXHGTzdf89",
                       "EBDCTXR2X7xdw389vv",
                       "ATGE761223m89glk03",
                       "aeaf970221hgt34304",
                       "mahc970513hgtrrs0t",
                       "AEAF970221HGTRGLx4",
                       "AEAF972421HGTRGLO4",
                       "MERA010733HGTNMNA9",
                       "mahc970513hwwrrs06",
                       "AFAA930918"
                       )
    print("\nDEMO DE CURP VALIDOS")
    for i in curpCorrectas:
        if (validaCURP(i)):
            print(f"El CURP [{i}] es valido")
        else:
            print(f"El CURP [{i}] es invalido")
    print("\nDEMO DE RFC INVALIDOS")
    for i in curpIncorrectas:
        if (validaCURP(i)):
            print(f"El CURP [{i}] es valido")
        else:
            print(f"El CURP [{i}] es invalido")
