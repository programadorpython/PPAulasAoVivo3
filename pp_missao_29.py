print('''1.	Carro híbrido é um tipo específico de carro. Escreva uma classe chamada CarroHibrido que herde da
classe Carro escrita anteriormente. Adicione um atributo chamado opcionais que armazene uma lista de opcionais 
de carro híbrido. Escreva um método para mostrar esses opcionais. Crie uma instância de CarroHibrido e chame 
esse método.''')

from Carros.carros import CarroHibrido

carro_hibrido = CarroHibrido('Fusion', 'Ford')
# print(carro_hibrido)
carro_hibrido.opcionais.append('Bateria 100')
carro_hibrido.opcionais.append('Carregador especial Mod. S')
carro_hibrido.carro_detalhes()
carro_hibrido.mostrar_opcionais()
print(carro_hibrido.modelo_carro)
print(carro_hibrido.numero_donos)

carro_hibrido_2 = CarroHibrido('Camry', 'Toyota')
# print(carro_hibrido_2)
carro_hibrido_2.opcionais.append('Bateria 150')
carro_hibrido_2.opcionais.append('Carregador especial Mod. T')
carro_hibrido_2.carro_detalhes()
carro_hibrido_2.mostrar_opcionais()
print(carro_hibrido_2.modelo_carro)
print(carro_hibrido_2.numero_donos)
