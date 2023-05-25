import random
from tda_lista import Lista, insertar, eliminar, busqueda, barrido, get_elements
from tda_hash import crear_tabla, agregar_ta, quitar_ta, buscar_ta, hash_division, bernstein

class Pokemon:
    def __init__(self, tipo, nivel):
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return f'Tipo: {self.tipo} - Nivel: {self.nivel}'

# Generar 800 Pokemon
tipos = ['Agua', 'Fuego', 'Tierra', 'Electrico', 'Normal', 'Fantasma']
pokemons = [Pokemon(random.choice(tipos), str(random.randint(100,999))) for _ in range(800)]

# Crear tablas hash
tabla1 = crear_tabla(1000)
tabla2 = crear_tabla(26)

# Funciones hash personalizadas
def hash_last_three(pokemon, tabla):
    return int(pokemon.nivel[-3:]) % len(tabla)

def hash_tipo(pokemon, tabla):
    return ord(pokemon.tipo[0].upper()) % len(tabla)

def comparar_pokemons(p1, p2):
    return int(p1.nivel) - int(p2.nivel)

# Cargar Pokemon en las tablas hash
for pokemon in pokemons:
    agregar_ta(tabla1, hash_last_three, pokemon)
    agregar_ta(tabla2, hash_tipo, pokemon, comparar_pokemons)

# Buscar y eliminar Fantasma-187
fantasma_187 = Pokemon('Fantasma', '187')

# Buscar en la primera tabla
pos = buscar_ta(tabla1, hash_last_three, fantasma_187)
if pos is not None:
    print('Fantasma-187 encontrado en la primera tabla. Procediendo a eliminar.')
    quitar_ta(tabla1, hash_last_three, fantasma_187)

# Buscar en la segunda tabla
pos = buscar_ta(tabla2, hash_tipo, fantasma_187)
if pos is not None:
    print('Fantasma-187 encontrado en la segunda tabla. Procediendo a eliminar.')
    quitar_ta(tabla2, hash_tipo, fantasma_187)

# Misión de asalto: Pokemon terminados en 78
print("\nMisión de asalto: Pokemon terminados en 78")
for i in range(len(tabla1)):
    for pokemon in get_elements(tabla1[i]):
        if pokemon.nivel.endswith('78'):
            print(pokemon)

# Misión de exploración: Pokemon terminados en 37
print("\nMisión de exploración: Pokemon terminados en 37")
for i in range(len(tabla1)):
    for pokemon in get_elements(tabla1[i]):
        if pokemon.nivel.endswith('37'):
            print(pokemon)

# Misión de custodia al Profesor Oak: Pokemon de tipo Tierra
print("\nMisión de custodia al Profesor Oak: Pokemon de tipo Tierra")
for i in range(len(tabla2)):
    for pokemon in get_elements(tabla2[i]):
        if pokemon.tipo == 'Tierra':
            print(pokemon)

# Misión de exterminación en Cueva Lava: Pokemon de tipo Fuego
print("\nMisión de exterminación en Cueva Lava: Pokemon de tipo Fuego")
for i in range(len(tabla2)):
    for pokemon in get_elements(tabla2[i]):
        if pokemon.tipo == 'Fuego':
            print(pokemon)

