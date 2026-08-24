# main.py

from pokemon import Pokemon
from pokedex import Pokedex
from treinador import Treinador


pokedex = Pokedex()

nome_treinador = input("Digite o nome do treinador: ")
treinador = Treinador(nome_treinador)


while True:
    print("\n===== POKÉDEX =====")
    print("1 - Cadastrar Pokémon")
    print("2 - Listar Pokémon")
    print("3 - Ver Pokémon capturados")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("CADASTRAR POKÉMON")

        nome = input("Nome do Pokémon: ")
        tipo = input("Tipo do Pokémon: ")
        nivel = int(input("Nível do Pokémon: "))
        capturado = input("O Pokémon foi capturado? (s/n): ")

        pokemon = Pokemon(nome, tipo, nivel, capturado)

        pokedex.adicionar_pokemon(pokemon)

        if capturado == "Sim":
            treinador.capturar_pokemon(pokemon)

        print("Pokémon cadastrado.")

    elif opcao == "2":
        print("POKÉMONS DA POKÉDEX")

        pokemons = pokedex.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon cadastrado.")
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())

    elif opcao == "3":
        print("POKÉMONS CAPTURADOS")

        pokemons = treinador.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon capturado.")
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())

    elif opcao == "0":
        print("Saindo da Pokédex.")
        break

    else:
        print("Opção inválida!")

