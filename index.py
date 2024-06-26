# Tipo de jogo
singleplayer = ["Assassin's Creed", "Zelda Tears of Kingdom", "Hogwarts Legacy", "The Witcher III", "Skyrim", "Resident Evil Village", "The Last of Us", "Five Night's at Freddy", "Alan Wake 2"]
multiplayer = ["It Takes Two", "Elder Scrolls Online", "Phasmaphobia"]

# Estilo de jogo
# 1 Aventura1
# 2 RPG
# 3 Terror
estilosDisponiveis = {
  1: ["Assassin's Creed", "Zelda Tears of Kingdom", "Hogwarts Legacy", "It Takes Two"],
  2: ["The Witcher III", "Skyrim", "Elder Scrolls Online"],
  3: ["Resident Evil Village", "Phasmaphobia", "The Last of Us", "Five Night's at Freddy", "Alan Wake 2"]
}

def sugerir_jogos():
    status = True
    while status:
        escolha = int(input("Digite aqui qual tipo de jogo você prefere:\n1. Single Player\n2. Multi Player\n"))
        if 0 < escolha < 3:
            a = singleplayer if escolha == 1 else multiplayer
            escolhaEstilo = int(input("\nDigite aqui qual gênero de jogo você prefere:\n1. Aventura\n2. RPG\n3. Terror\n"))
            if 0 < escolhaEstilo < 4:
                b = estilosDisponiveis[escolhaEstilo]
                resultado = comparar(a, b)
                print("\nSugestões de jogos para você:")
                for jogo in resultado:
                    print(jogo)
                status = False
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

def comparar(a, b):
    resultado = [x for x in a if x in b]
    return resultado

def adicionar_jogo():
    jogoNovo = input("Digite aqui o nome do jogo novo: ")
    escolha = int(input("Digite aqui qual tipo de jogo você adicionou:\n1. Single Player\n2. Multi Player\n"))
    escolhaEstilo = int(input("\nDigite aqui qual gênero de jogo do jogo que você adicionou:\n1. Aventura\n2. RPG\n3. Terror\n"))
    
    if escolha == 1: 
        singleplayer.append(jogoNovo) 
    else: 
        multiplayer.append(jogoNovo)
    
    if escolhaEstilo == 1:
        estilosDisponiveis[1].append(jogoNovo) 
    elif escolhaEstilo == 2: 
        estilosDisponiveis[2].append(jogoNovo) 
    else: 
        estilosDisponiveis[3].append(jogoNovo)
    print("Jogo adicionado com sucesso!")
statusMenu = True
def main():
    while statusMenu:
        print("\nMenu:")
        print("1. Sugestão de Jogos")
        print("2. Adicionar Jogo")
        print("3. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            sugerir_jogos()
        elif opcao == 2:
            adicionar_jogo()
        elif opcao == 3:
            print("Obrigado por usar!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()