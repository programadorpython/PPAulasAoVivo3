print('''
1.	Usando sua classe Carro criada no ultimo exercício, acrescente um atributo chamado numero_donos com valor default 0.
Crie uma instância chamada meu_carro a partir dessa classe. Apresente o número de donos do carro, em seguida,
mude esse valor e exiba-o novamente.

a. Crie um método chamado setar_numero_donos() que permita definir um número de donos do carro.
Chame esse método com um novo número e mostre o valor novamente.
b. Adicione um método chamado incrementar_numero_donos() que permita incrementar o número de donos do carro.
Chame esse método com qualquer número que você quiser e que represente quantos donos possuíram o carro.
''')


class Carro():
    """
    Uma classe para modelar um carro
    """

    def __init__(self, modelo_carro, fabricante):
        """
        Inicializa um carro
        :param modelo_carro: string
        :param fabricante: string
        :param numero_donos: int (valor default: 0)
        """
        self.modelo_carro = modelo_carro
        self.fabricante = fabricante
        self.numero_donos = 0


    def carro_detalhes(self):
        """
        Mostra um resumo com dados do carro
        :return:
        """
        msg = f"Modelo: {self.modelo_carro}, Fabricante: {self.fabricante}"
        print(f"\n{msg}")

    def carro_concluido(self):
        """
        Mostra mensagem que o carro está pronto
        :return:
        """
        msg = f"{self.modelo_carro} está pronto para ser vendido!"
        print(f"\n{msg}")

    def setar_numero_donos(self, num_donos):
        """
        Método para alterar o número de donos
        :param num_donos: int
        :return:
        """
        self.numero_donos = num_donos

    def incrementar_numero_donos(self, num_incremento):
        """
        Método para incrementar o número de donos
        :param num_incremento: int
        :return:
        """
        self.numero_donos += num_incremento


fusca = Carro('fusca', 'VW')
print("Exibindo número de donos")
print(fusca.numero_donos)
fusca.numero_donos = 1
print(fusca.numero_donos)
fusca.setar_numero_donos(3)
print(fusca.numero_donos)
print("Exibindo número de donos com incremento")
fusca.incrementar_numero_donos(1)
print(fusca.numero_donos)

'''
2.	A sua classe Animal criada anteriormente, adicione um atributo chamado anos_no_zoo. Escreva um método chamado
incrementar_anos_zoo() que incremente o valor de anos_no_zoo em 1. Escreva outro método chamado resetar_anos_zoo()
que volte o valor anos_no_zoo para 0.
a.Crie uma instância da classe Animal e chame o incremente_anos_zoo() várias vezes. Exbia o valor de anos_no_zoo
para ter certeza que ele foi incrementado de forma correta. Em seguida chame o resetar_anos_zoo(). Exiba
anos_no_zoo novamente para ver o valor com 0.'''






