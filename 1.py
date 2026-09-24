from abc import ABC, abstractmethod


class notificacion(ABC):

    def __init__(self, tipo_canal):
        self.tipo_canal = tipo_canal
        self.destino = ""
        self.contenido = ""

    @abstractmethod
    def ejecutar_envio(self):
        pass


class CorreoElectronico(notificacion):

    def __init__(self):
        super().__init__("Correo Electrónico")
        self.asunto = ""

    def _es_valido(self):
        return "@" in self.destino and "." in self.destino

    def solicitar_datos(self):
        print()
        print(f"Configuración de {self.tipo_canal}")
        self.destino = input("Ingrese el correo del destinatario: ").strip()
        self.asunto = input("Ingrese el asunto: ").strip()
        self.contenido = input("Ingrese el cuerpo del mensaje: ").strip()

    def ejecutar_envio(self):
        if not self._es_valido():
            print(
                f"[X] Error de envío: '{self.destino}' no es una dirección de correo válida."
            )
            return False

        print()
        print(f"ENVIANDO: {self.tipo_canal.upper()}")
        print(f"Destinatario : {self.destino}")
        print(f"Asunto       : {self.asunto}")
        print(f"Mensaje      : {self.contenido}")
        print()
        return True


class SMS(notificacion):

    def __init__(self):
        super().__init__("Mensaje SMS")

    def _es_valido(self):
        return self.destino.isdigit() and len(self.destino) == 10

    def solicitar_datos(self):
        print()
        print(f"Configuración de {self.tipo_canal}")
        self.destino = input("Ingrese el número de teléfono (10 dígitos): ").strip()
        self.contenido = input("Ingrese el texto del SMS: ").strip()

    def ejecutar_envio(self):
        if not self._es_valido():
            print(
                f"[X] Error de envío: '{self.destino}' debe contener exactamente 10 dígitos numéricos."
            )
            return False

        print()
        print(f"ENVIANDO: {self.tipo_canal.upper()}")
        print(f"Línea destino : {self.destino}")
        print(f"Contenido     : {self.contenido}")
        print()
        return True


class notificacionapp(notificacion):

    def __init__(self):
        super().__init__("Notificación Push")

    def _es_valido(self):
        return len(self.destino) > 0

    def solicitar_datos(self):
        print()
        print(f"Configuración de {self.tipo_canal}")
        self.destino = input("Ingrese el ID de usuario de la App: ").strip()
        self.contenido = input("Ingrese la alerta Push: ").strip()

    def ejecutar_envio(self):
        if not self._es_valido():
            print("[X] Error de envío: El ID de usuario no puede estar vacío.")
            return False

        print()
        print(f"ENVIANDO: {self.tipo_canal.upper()}")
        print(f"ID Usuario : {self.destino}")
        print(f"Alerta     : {self.contenido}")
        print()
        return True


notificaciones = [CorreoElectronico(), SMS(), notificacionapp()]

print("GESTOR DE ENVÍO DE NOTIFICACIONES")

for notificacion in notificaciones:
    notificacion.solicitar_datos()

print()
print("Procesando envíos...")
for notificacion in notificaciones:
    notificacion.ejecutar_envio()

