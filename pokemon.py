class Pokemon:
    def __init__(self, nome, tipo, nivel, capturado):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.capturado = capturado
    def imprimir_dados(self):
        return f"Nome do Pokémon: {self.nome}, Tipo: {self.tipo}, Nível do Pokémon: {self.nivel}, Status de Captura: {self.capturado}."
