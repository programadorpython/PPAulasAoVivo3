print('''1.	Crie uma classe chamada Carro. O método __init__() do Carro deve armazenar os atributos modelo_carro e
fabricante. Crie um método chamado carro_detalhes() que mostre essas duas informações. Crie um método
carro_concluido() que mostre uma mensagem que o carro está pronto para ser comercializado. Crie uma instância
chamada carro a partir de sua classe. Mostre os dois atributos e chame os dois métodos.''')
print()

from Carros.carros import Carro
from Animais.animais import Animal


carro = Carro('Fiesta', 'Ford')
# print(carro)
print(carro.modelo_carro)
print(carro.fabricante)
carro.carro_detalhes()
carro.carro_concluido()

carro_2 = Carro('Corolla', 'Toyota')
# print(carro_2)
carro_2.carro_detalhes()
carro_2.carro_concluido()

print()
print()
print(''' 2. Com a classe Carro anterior, crie três instâncias diferentes da classe e chame o carro_detalhes()
para cada instância.''')

carro_3 = Carro('Civic', 'Honda')
carro_3.carro_detalhes()

print('''
3. Crie uma classe chamada Animal. Crie dois atributos nome e idade e então crie vários outros atributos como
sexo, cor, etc. Faça um método animal_detalhes() que mostre um resumo das informações do animal. Faça outro
método mensagem() que mostre uma mensagem usando o nome do animal. Crie várias instâncias que representem vários
animais e chame os dois métodos para cada animal.
''')
print()




cachorro = Animal('pitoco', 5, 'macho', 'marron', 'cachorro', 'mamíferos')
cachorro.animal_detalhes()
cachorro.mensagem()

gato = Animal('tom', 3, 'macho', 'cinza', 'gato', 'mamíferos')
gato.animal_detalhes()
gato.mensagem()
