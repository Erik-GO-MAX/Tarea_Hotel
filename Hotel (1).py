#definimos una clase para la habitacion
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservada = False

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - {'Reservada' if self.reservada else 'Disponible'}"

#clase para el huesped
class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Huésped: {self.nombre}"


class Reservacion:
    def __init__(self):
        self.habitaciones = []
        self.huespedes = []
#metodo para que el huesped reserve su habitacion, numero y tipo de habitacion
    def agregar_habitacion(self, numero, tipo):
        habitacion = Habitacion(numero, tipo)
        self.habitaciones.append(habitacion)

    def agregar_huesped(self, nombre):
        huesped = Huesped(nombre)
        self.huespedes.append(huesped)
#metodo para reservar una habitacion y que nos muestre solo las que estan sin reservar
    def reservar_habitacion(self, numero_habitacion, nombre_huesped):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion), None)
        huesped = next((h for h in self.huespedes if h.nombre == nombre_huesped), None)
#numero de habitacion que quiere el  huesped o si la habitacion existe o no
        if habitacion and not habitacion.reservada:
            if huesped:
                habitacion.reservada = True
                print(f"{nombre_huesped} ha reservado la {habitacion}")
            else:
                print(f"No se ha encontrado el huésped {nombre_huesped}")
        else:
            print(f"La habitación {numero_habitacion} no está disponible o no existe.")

    def mostrar_habitaciones_disponibles(self):
        disponibles = [str(h) for h in self.habitaciones if not h.reservada]
        if disponibles:
            print("\nHabitaciones disponibles:")
            for hab in disponibles:
                print(hab)
        else:
            print("No hay habitaciones disponibles.")



sistema_reservas = Reservacion()

"""Agregar habitaciones"""
sistema_reservas.agregar_habitacion(208, "Individual")
sistema_reservas.agregar_habitacion(130, "Doble")
sistema_reservas.agregar_habitacion(285, "Individual")

"""Agregar huéspedes"""
sistema_reservas.agregar_huesped("jorge nitales")
sistema_reservas.agregar_huesped("alma marcela gozo")

"""Mostrar habitaciones disponibles"""
sistema_reservas.mostrar_habitaciones_disponibles()

""" Reservar una habitación"""
sistema_reservas.reservar_habitacion(208, "jorge nitales")

""""Mostrar habitaciones disponibles nuevamente"""
sistema_reservas.mostrar_habitaciones_disponibles()