# DESCRIPTION: Clase Cliente que realiza las operaciones de backend de conexión de sockets
#                por TCP y configuración del mismo (ip, puerto, protocolo de envio).
# AUTHOR: Félix Armenta Aguiñaga - IECA PADTS 3

from estudiante import Estudiante
import socket
import pickle


class Cliente:
    def __init__(self, ip=socket.gethostname(), puerto=9999):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__ip = ip
        self.__puerto = puerto

    def getIP(self):
        return self.__ip

    def getPuerto(self):
        return self.__puerto

    def setIP(self, ip):
        self.__ip = ip

    def setPuerto(self, puerto):
        self.__puerto = puerto

    def conectar(self):
        self.clientSocket.connect((self.getIP(), self.getPuerto()))

    def desconectar(self):
        self.clientSocket.close()

    def enviar(self, objeto):
        objSerializado = pickle.dumps(objeto)

        if isinstance(objeto, Estudiante):
            self.clientSocket.send(objSerializado)
            res = self.clientSocket.recv(1024)  # Espera resupesta
            return res.decode()
        else:
            self.clientSocket.send(b"INI")
            res = self.clientSocket.recv(1024)
            print(res.decode())

            if len(objSerializado) < 1024:
                self.clientSocket.send(objSerializado)
                # esperar respuesta
                res = self.clientSocket.recv(1024)
                return res.decode()
            else:
                continuar = True
                inicio = 0
                while continuar:
                    # Tomar 1024 bytes del objeto serializado
                    chunk = objSerializado[inicio: inicio + 1024] # Toma de 0 a 1023
                    if not chunk:
                        continuar = False
                        continue
                    self.clientSocket.send(chunk)
                    res = self.clientSocket.recv(1024)
                    print(res.decode())

                    inicio += 1024

            self.clientSocket.send(b"FIN")
            res = self.clientSocket.recv(1024)  # Respuesta paquete FIN
            print(res.decode())

            res = self.clientSocket.recv(1024)  # Respuesta de validacion del archivo
            return res.decode()


if __name__ == '__main__':
    c = Cliente("3.16.226.150", 9998)
    c.conectar()
    alumno = Estudiante("Felix Armenta A", "3armenta@gmail.com", "PADTS_3")
    respuesta = c.enviar(alumno)

    print(respuesta)

    f = open("test.zip", "rb")
    respuesta = c.enviar(f.read())
    print(respuesta)
    c.desconectar()
