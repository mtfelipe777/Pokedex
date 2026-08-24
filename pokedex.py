class Pokedex:
    def __init__(self):
        self.pokemons = []

    def adicionar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def listar_pokemons(self):
        return self.pokemons
    