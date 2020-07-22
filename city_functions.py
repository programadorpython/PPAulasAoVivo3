'''1.	Cidade, país - Escreva uma função que aceite dois parâmetros: o nome de uma cidade e o nome de um país.
A função deve devolver uma única string no formado Cidade, País, por exemplo, Santiago, Chile. Armazene a função
em um módulo chamado city_functions.py.
a. Crie um arquivo de nome test_cities.py que teste a função que você acabou de escrever (lembre-se de que
é necessário importar unittest e a função que você quer testar). Escreva um método chamado test_cidade_pais()
para conferir se a chamada à sua função com valores como 'santiago' e 'chile' resulta na string correta.
Execute testes.py e garanta que test_cidade_pais() passe no teste.'''

def cidade_pais(cidade, pais):
    """
    Retorna uma string tipo 'Santiago, Chile'
    :param cidade: string
    :param pais: string
    :return: string
    """
    return f"{cidade.title()}, {pais.title()}"