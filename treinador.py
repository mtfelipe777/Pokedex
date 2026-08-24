from equipe import Equipe
class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.equipe = Equipe()

    def capturar_pokemon(self, pokemon):
        self.equipe.adicionar_pokemon(pokemon)

    def listar_pokemons(self):
        return self.equipe.listar_pokemons()