# Polimorfismo en OOP en programación orientada a objetos permite que métodos con el mismo nombre
# tengan comportamientos distintos dependiendo de la clase que lo implementa

class Notificacion:
    def __init__(self, remitente, destinatario, mensaje):
        self.remitente = remitente
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar_mensaje(self):
        print(f"Remitente de mensaje: {self.remitente}")
        print(f"Destinatario de mensaje: {self.destinatario}")
        print(f"Mensaje:\n{self.mensaje}")

class NotificacionEmail(Notificacion):
    def __init__(self, remitente, destinatario, mensaje, asunto):
        super().__init__(remitente, destinatario, mensaje)
        self.asunto = asunto
    
    def enviar_mensaje(self):
        print(f"\nAsunto: {self.asunto}")
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje:\n{self.mensaje}")

class NotificacionSMS(Notificacion):
    def __init__(self, remitente, destinatario, mensaje):
        super().__init__(remitente, destinatario, mensaje)
        if not isinstance(destinatario, int):
            raise ValueError("El destinatario deber ser un número telefonico.")
        self.destinatario = destinatario

        if len(self.mensaje) > 70:
            print("El mensaje excede los 70 caracteres, será truncado.")
            self.mensaje = mensaje[:70]

    def enviar_mensaje(self):
        print(f"Destinatario: {self.destinatario}")
        print(f"{self.mensaje}")

class NotificacionPUSH(Notificacion):
    def __init__(self, remitente, destinatario, mensaje):
        super().__init__(remitente, destinatario, mensaje)
        if len(self.mensaje) > 50:
            print("El mensaje excede los 50 caracteres, será truncado.")
            self.mensaje = mensaje[:50]


    def enviar_mensaje(self):
        print(f"{self.remitente}")
        print(f"{self.destinatario}")
        print(f"{self.mensaje}")


email = NotificacionEmail("Miguel", "Camila", "Nos vemos mañana", "Reunión")
sms = NotificacionSMS("Banco", 3115551234, "Tu código es 123456. No lo compartas con nadie.")
push = NotificacionPUSH("App XYZ", "Usuario123", "Tienes una nueva recompensa acumulada. Reclámala ahora!")

email.enviar_mensaje()
sms.enviar_mensaje()
push.enviar_mensaje()
