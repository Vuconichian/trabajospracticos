from datetime import datetime
from pila_para_ej import Pila

class Cola:
    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def attention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            first_element = self.attention()
            self.arrive(first_element)


class Notification:
    def __init__(self, time, app, message):
        self.time = time
        self.app = app
        self.message = message


def eliminar_notificaciones_facebook(cola):
    elementos_eliminar = []
    while cola.size() > 0:
        notificacion = cola.attention()
        if notificacion.app != "Facebook":
            elementos_eliminar.append(notificacion)

    for elemento in elementos_eliminar:
        cola.arrive(elemento)


def twitter_python(cola):
    notif_verificadas = 0

    while notif_verificadas < cola.size():
        notificacion = cola.attention()
        if notificacion.app == "Twitter" and "Python" in notificacion.message:
            print(f"Hora: {notificacion.time}")
            print(f"Aplicación: {notificacion.app}")
            print(f"Mensaje: {notificacion.message}")
            print()

        cola.arrive(notificacion)
        notif_verificadas += 1


def almacenar_notif(cola):
    pila_temp = Pila()
    contador = 0

    while cola.size() > 0:
        notificacion = cola.attention()
        hora = datetime.strptime(notificacion.time, "%H:%M").time()

        hora_inicio = datetime.strptime("11:43", "%H:%M").time()
        hora_fin = datetime.strptime("15:57", "%H:%M").time()

        if hora_inicio <= hora <= hora_fin:
            contador += 1
            pila_temp.push(notificacion)
        else:
            pila_temp.push(notificacion)

    return contador, pila_temp


cola_notificaciones = Cola()

cola_notificaciones.arrive(Notification("10:30", "Facebook", "Notificación 1"))
cola_notificaciones.arrive(Notification("11:15", "Spotify", "Notificación 2"))
cola_notificaciones.arrive(Notification("12:20", "Facebook", "Notificación 3"))
cola_notificaciones.arrive(Notification("13:45", "Twitter", "Notificación 4"))
cola_notificaciones.arrive(Notification("14:50", "Youtube", "Notificación 5"))
cola_notificaciones.arrive(Notification("15:30", "LinkedIn", "Notificación 6"))
cola_notificaciones.arrive(Notification("16:10", "Facebook", "Notificación 7"))
cola_notificaciones.arrive(Notification("17:20", "Twitter", "Python"))

print("Notificaciones sin facebook: ")
eliminar_notificaciones_facebook(cola_notificaciones)

def mostrar_notificaciones(cola_notificaciones):
    lista_aux = []
    while cola_notificaciones.size() > 0:
        notificacion = cola_notificaciones.attention()
        print(f'Hora: {notificacion.time}, Aplicación: {notificacion.app}, Mensaje: {notificacion.message}')
        lista_aux.append(notificacion)
    
    for notif in lista_aux:
        cola_notificaciones.arrive(notif)

mostrar_notificaciones(cola_notificaciones)

print()

print("Notificaciones de Twitter que contienen Python: ")
twitter_python(cola_notificaciones)

cont, pila = almacenar_notif(cola_notificaciones)

print(f'Cantidad de notificaciones entre las 11:43 y las 15:57: {cont}\n')

print('Notificaciones entre ese horario:\n')
while pila.size() > 0:
    notificacion = pila.pop()
    print(f"Hora: {notificacion.time}")
    print(f"Aplicación: {notificacion.app}")
    print(f"Mensaje: {notificacion.message}\n")

