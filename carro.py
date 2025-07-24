class Carro:
    # Construindo a classe Carro com seus atributos
    def __init__(self, marca, modelo, ano, cor, ligado=False, velocidade=0):
        self.marca = marca          # Marca do carro (ex: Ford, Toyota)
        self.modelo = modelo        # Modelo do carro (ex: Fiesta, Corolla)
        self.ano = ano              # Ano de fabricação
        self.cor = cor              # Cor do carro
        self.ligado = ligado        # Estado ligado/desligado (True/False)
        self.velocidade = velocidade # Velocidade atual do carro (km/h)

    # Método para exibir todos os detalhes do carro
    def exibir_resultados(self):
        print("\nDetalhes ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Ligado: {'Sim' if self.ligado else 'Não'}")  # Exibe "Sim" se ligado for True, senão "Não"
        print(f"Quilometragem: {self.velocidade} km/h")      # Exibe a velocidade atual

    # Método para ligar o carro
    def ligar(self):
        self.ligado = True
        print("Carro ligado")

    # Método para desligar o carro, só funciona se velocidade for 0
    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print("O carro foi desligado")
        else:
            print("Pare o carro antes de desligar")

    # Método para acelerar o carro, somando a velocidade passada ao atributo velocidade
    def acelerar(self, valor):
        if self.ligado:
            self.velocidade += valor
            print(f"O carro acelerou {valor} Km/h. Velocidade atual {self.velocidade} Km/h")
        else:
            print("O carro está desligado. Ligue antes de acelerar")

    # Método para frear o carro, reduzindo a velocidade conforme o valor informado
    def frear(self, valor):
        if self.velocidade < valor:
            self.velocidade = 0
            print("O carro zerou a velocidade")
        else:
            self.velocidade -= valor
            print(f"O carro reduziu a velocidade para {self.velocidade} Km/h")

    # Método especial para mostrar a representação em string do objeto (útil para print)
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    # Método especial chamado quando o objeto é destruído pelo Python
    def __del__(self):
        print("Destruindo o carro da memória...")


# Entrada de dados do usuário para criar o objeto Carro
marca = input("Marca: ")
modelo = input("Modelo: ")
ano = int(input("Ano: "))
cor = input("Cor: ")
ligar = input("Ele está ligado [S/N]: ").strip().upper()[0]  # Pega só a primeira letra maiúscula
velocidade = float(input("Qual é sua velocidade atual: "))

# Convertendo o input para booleano para o atributo 'ligado'
if ligar == "S":
    ligar = True
else:
    ligar = False

# Criando o objeto carro com os valores informados
carro = Carro(marca, modelo, ano, cor, ligado=ligar, velocidade=velocidade)

# Pergunta se deseja exibir os detalhes do carro
exibir = input("Deseja exibir detalhes [S/N]: ").strip().upper()[0]
if exibir == "S":
    carro.exibir_resultados()

# Pergunta se deseja ligar o carro (mesmo que já esteja ligado)
ligado = input("Verificar se ele está ligado [S/N]: ").strip().upper()[0]
if ligado == "S":
    carro.ligar()

# Pergunta se deseja acelerar e o quanto deseja acelerar
deseja_acelerar = input("Deseja acelerar [S/N]: ").strip().upper()[0]
if deseja_acelerar == "S":
    carro.acelerar(int(input("Quantos você quer acelerar (Km/h)?: ")))

# Pergunta se deseja frear e o quanto deseja frear
deseja_freiar = input("Deseja frear [S/N]: ").strip().upper()[0]
if deseja_freiar == "S":
    carro.frear(int(input("Quantos você vai querer reduzir (Km/h)?: ")))
