from equipe import Equipe
class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.pokemons = []
        self.equipe = Equipe()

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def listar_pokemons(self):
        return self.pokemons