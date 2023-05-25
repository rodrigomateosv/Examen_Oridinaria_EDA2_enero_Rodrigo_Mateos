
# Importando librerías
import unittest

class Pokeball:
    def __init__(self, nombre, peso, precio, fecha_fabricacion):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print(f'La Pokeball {self.nombre} se ha creado con éxito.')

    def __str__(self):
        return f"Pokeball: {self.nombre}, Peso: {self.peso}g, Precio: {self.precio}$, Fecha de fabricación: {self.fecha_fabricacion}"

class TestEjercicios(unittest.TestCase):

    def setUp(self):
        self.pokeballs = [
            Pokeball('pokeball1', 50, 200, '2023-01-01'),
            Pokeball('pokeball2', 50, 300, '2023-02-01'),
            Pokeball('pokeball3', 50, 400, '2023-03-01'),
            Pokeball('pokeball4', 50, 500, '2023-04-01'),
        ]

        # Ordenando las Pokeballs por fecha de fabricación
        self.pokeballs.sort(key=lambda x: x.fecha_fabricacion)

    def test_pokeball_data(self):
        # Mostrando datos de todas las Pokeballs
        for pokeball in self.pokeballs:
            print(pokeball)
            
        # Modificando el precio de la primera Pokeball
        self.pokeballs[0].precio = 1000
        print("\nDespués de modificar el precio:")
        for pokeball in self.pokeballs:
            print(pokeball)

if __name__ == "__main__":
    unittest.main()


            
    