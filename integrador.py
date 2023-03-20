#7
import re

class Cuenta:
    def __init__(self, titular=None, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not valor:
            print("El titular no puede estar vacío.")
        else:
            self._titular = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:
            print("La cantidad no puede ser negativa.")
        else:
            self._cantidad = valor

    def mostrar(self):
        print(f"Titular: {self.titular}\nCantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("No se puede ingresar una cantidad negativa.")
        else:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad < 0:
            print("No se puede retirar una cantidad negativa.")
        elif self.cantidad < cantidad:
            print("No hay suficiente saldo en la cuenta.")
        else:
            self.cantidad -= cantidad
            print("Retiro realizado correctamente.")


# Ejemplo de uso
cuenta1 = Cuenta()
cuenta1.titular = "Walter Benjamin"
cuenta1.cantidad = 10000.0
cuenta1.mostrar()

cuenta1.ingresar(5000.0)
cuenta1.mostrar()

cuenta1.retirar(20000.0)
cuenta1.mostrar()

cuenta1.retirar(5000.0)
cuenta









#8
import re

class CuentaJoven(CuentaBancaria):
    
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, value):
        if not re.match(r'^\d+(\.\d+)?$', str(value)):
            raise ValueError("La bonificación debe ser un número.")
        value = float(value)
        if value < 0 or value > 100:
            raise ValueError("La bonificación debe ser un número entre 0 y 100.")
        self._bonificacion = value    
    
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25
    
   def retirar(self, cantidad):
    if not self.es_titular_valido():
        raise ValueError("No se puede retirar dinero de una cuenta joven con un titular no válido.")
    if not re.match(r'^\d+(\.\d+)?$', str(cantidad)):
        raise ValueError("La cantidad a retirar debe ser un número.")
    cantidad = float(cantidad)
    if cantidad <= 0:
        raise ValueError("La cantidad a retirar debe ser mayor que cero.")
    if cantidad > self.cantidad:
        raise ValueError("La cantidad a retirar excede el saldo de la cuenta.")
    self.cantidad -= cantidad * (1 - self.bonificacion / 100)

    
    def mostrar(self):
        return f"Cuenta Joven: {super().mostrar()} Bonificación: {self.bonificacion}%"

    cuenta_joven = CuentaJoven(Persona("Walter", 20), 10000, 10)

# Comprobamos que la bonificación ha sido correctamente validada
try:
    cuenta_joven.bonificacion = "20%"
except ValueError as e:
    print(f"Error: {e}")  # Debe imprimir "La bonificación debe ser un número."

try:
    cuenta_joven.bonificacion = 150
except ValueError as e:
    print(f"Error: {e}")  # Debe imprimir "La bonificación debe ser un número entre 0 y 100."

# Comprobamos que el método "es_titular_valido" funciona correctamente
print(cuenta_joven.es_titular_valido())  # Debe imprimir False

cuenta_joven.titular.edad = 20
print(cuenta_joven.es_titular_valido())  # Debe imprimir True

# Comprobamos que el método "retirar" funciona correctamente
cuenta_joven.retirar(5000)  # Debe imprimir "No se puede retirar dinero de una cuenta joven con un titular no válido."

cuenta_joven.titular.edad = 26
cuenta_joven.retirar(5000)  # Debe retirar 5000 sin problemas

# Comprobamos que el método "mostrar" funciona correctamente
print(cuenta_joven.mostrar())  # Debe imprimir "Cuenta Joven: Titular: Walter, Edad: 20, Cantidad: 5000.0 Bonificación: 10%"
