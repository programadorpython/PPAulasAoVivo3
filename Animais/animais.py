class Animal:
    """
    Modelando um animal
    """

    def __init__(self, nome, idade, sexo, cor, tipo, classe):
        """
        Inicializa um animal
        :param nome: string
        :param idade: int
        :param sexo: string
        :param cor: string
        :param tipo: string
        :param classe: sring
        """
        self.nome = nome.title()
        self.idade = idade
        self.sexo = sexo
        self.cor = cor
        self.tipo = tipo.title()
        self.classe = classe.title()

    def animal_detalhes(self):
        """
        Mostra detalhes do animal
        :return:
        """
        mensagem = f"O animal do tipo {self.tipo} é da classe {self.classe}: " \
                   f"\n\tnome: {self.nome} " \
                   f"\n\tidade: {self.idade} " \
                   f"\n\tsexo: {self.sexo} " \
                   f"\n\tcor: {self.cor}"
        print(f"\n{mensagem}")

    def mensagem(self):
        """
        Mostra mensagem com o nome do animal
        :return:
        """
        saudacao = f"Olá {self.nome}, seja bem vindo ao nosso Pet Shop!"
        print(f"\n{saudacao}")
