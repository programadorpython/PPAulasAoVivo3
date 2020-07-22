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