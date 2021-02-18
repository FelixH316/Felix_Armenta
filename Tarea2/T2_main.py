# DESCRIPCION:  Main de la Tarea 3 - Validacion de correo, telefono,
#               CURP y RFC a través de expresiones regulares.
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

#from paqueteT2 import validaExp
from paqueteT2.validaExp import validaCorreo
from paqueteT2.validaExp import validaTel
from paqueteT2.validaExp import validaRFC
from paqueteT2.validaExp import validaCURP

if __name__ == '__main__':
    resultado = ("invalido", "valido")
    print("\nIntroduce tu correo: ", end=' ')
    correo = input()

    print("Introduce tu numero de telefono: ", end=' ')
    telefono = input()

    print("Introduce tu RFC: ", end=' ')
    rfc = input()

    print("Introduce tu CURP: ", end=' ')
    curp = input()

    print(f"\nEl correo {correo} es {resultado[validaCorreo(correo)]}")
    print(f"El numero de telefono {telefono} es {resultado[validaTel(telefono)]}")
    print(f"El RFC {rfc} es {resultado[validaRFC(rfc)]}")
    print(f"El CURP {curp} es {resultado[validaCURP(curp)]}")
