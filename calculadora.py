# Importar as bibliotecas
import os       
import clipboard

# Funcao de limpar tela
def limpar_tela():
    os.system('cls')

limpar_tela()

# Calculo do valor do CTe
valor_descarga = float(input("Digite o valor: "))
valor_icms = float(input("Digite o valor do ICMS (7 , 12 ou 17): "))

valor_icms = (100 - valor_icms) / 100
possui_pis = input("Tem pis?: ")
pis = 0.9075

if possui_pis in["S", "s", "1"]:
    valor_com_imposto = valor_descarga / valor_icms / pis
    
elif possui_pis in ["N", "n", "0", ""]:
    valor_com_imposto = valor_descarga / valor_icms
    
# Formatar o valor com apenas 2 numeros apos a virgula
valor_com_imposto = (f"{valor_com_imposto:.2f}")

print(valor_com_imposto)

# Copiar o valor para o CTRL+C
clipboard.copy(valor_com_imposto)