import random
# Personagem: Classe Mãe
# Herói: controlado pelo usuário
# Inimigo: adversario do usuário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) # baseado no nivel
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__nivel = 0
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        self.__qtd_ataque_especial = 2

    def get_habilidade(self):
        return self.__habilidade
    
    def get_qtd_ataque_especial(self):
        return self.__qtd_ataque_especial

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo): 
        dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
    
    def verificar_ataques_especiais(self):
        if self.__qtd_ataque_especial > 0:
            self.__qtd_ataque_especial -= 1
            return True
        return False

    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
    
class Jogo:
    """ Classe orquestradora do jogo """

    def __init__(self):
        self.heroi = Heroi(nome="Matheus", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Lananda", vida=100, nivel=5, tipo="Lacraia")

    def iniciar_batalha(self):
        """ Fazer a gestã da batalha em turnos """
        print("Iniciando batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens")
            print("\nHerói")
            print(self.heroi.exibir_detalhes())
            print("\nInimigo")
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("\n1. Ataque Normal\n2. Ataque Especial\n3. Consultar Quantidade de Ataques Especiais\nEscolha: ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                if self.heroi.verificar_ataques_especiais():
                    self.heroi.ataque_especial(self.inimigo)
                else:
                    print("\nVocê não possui ataques especiais disponiveis. Use ataques normais")
                    continue
            elif escolha == '3':
                print(f"\nVocê tem disponivel {self.heroi.get_qtd_ataque_especial()} ataques especiais!")
                continue
            else:
                print("\nOpção invalida. Tente novamente!")
                continue

            # Ataque do inimigo
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")

# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
