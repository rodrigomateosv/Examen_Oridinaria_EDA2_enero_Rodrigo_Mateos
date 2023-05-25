import random

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.PS = random.randint(50, 100)
        self.ataque = random.randint(50, 100)
        self.defensa = random.randint(50, 100)
        self.ataque_especial = random.randint(50, 100)
        self.defensa_especial = random.randint(50, 100)
        self.velocidad = random.randint(50, 100)
        print(f'El Pokemon {self.nombre} se ha creado con éxito.')
        
    def clasificacion(self):
        if self.tipo == "Agua":
            print(f'{self.nombre} es un Pokemon de agua.')
        elif self.tipo == "Fuego":
            print(f'{self.nombre} es un Pokemon de fuego.')
        elif self.tipo == "Planta":
            print(f'{self.nombre} es un Pokemon de planta.')
        else:
            print(f'{self.nombre} es un Pokemon de tipo {self.tipo}.')

import unittest

class TestEjercicios(unittest.TestCase):
    def setUp(self):
        self.lista_pokemons = [
            Pokemon("Bulbasaur", "Planta"), 
            Pokemon("Charmander", "Fuego"), 
            Pokemon("Squirtle", "Agua"), 
            Pokemon("Pikachu", "Electrico"),
            # Añade más Pokemons aquí si lo deseas.
        ]

    def test_pokemon(self):
        for pokemon in self.lista_pokemons:
            pokemon.clasificacion()  # Llamar al método clasificacion para cada Pokemon.

if __name__ == "__main__":
    unittest.main()
