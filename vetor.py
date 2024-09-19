# criando a class chamada carro
class Carro:
    def __init__(self, fabricante, modelo, cor, valor, ano, placa):
        # definindo os atributos
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.ano = ano
        self.placa = placa


# criando objeto
celta = Carro("gm", "celta", "azul", 12000, 2012, "BDNI580")
print("carro", celta.modelo, "ano:", celta.ano)
carro1 = Carro("VW", "nivs", "prata", 85000, 2020, "ANCI538")
print("placa", carro1.placa)