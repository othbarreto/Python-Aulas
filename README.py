# Python-Aulas
Testes feitos em Python

valor_compra = float(input("Digite o valor da compra:"))

valor_frete = float(input("Digite o valor do frete:"))

cal_compra_frete = valor_compra + valor_frete

cliente_cadastrado = input("Cliente cadastrado no prog. de fidelidade ?")

if cal_compra_frete > 100 or cliente_cadastrado == "S":

  input("Pode usar o cupom")

elif cal_compra_frete < 100 and cliente_cadastrado == "N":

  input("Não pode usar cupom")

