#Programa estoque com frete
#Variaveis de memória
vcont = "5"
vproduto = ""
vquantidade = 0
vvalor = 0.0
vpeso= 0.0
#criando lista
lproduto= []
lvalor= []
lquantidade= []
lpeso= []
print("Sistema vendas")
while vcont== "s":
    vproduto= input("Digite o produto: ")

vvalor= float(input("Valor: "))
vquantidade= int(input("quant: "))
vpeso= float(input("peso: "))
lproduto.append(vproduto)
lvalor.append(vvalor)
lquantidade.append(vquantidade)
lpeso.append(vpeso)
vcont= input("Deseja continuar <s/n>:")
print("------------------------------")
print("----calculando peso-----")
