#Função para inverter a string
def inverter_string(s):
    #Inicializa uma string vazia para armazenar o resultado
    invertida = ""
    
    #Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

entrada = input('Digite uma mensagem ou palavra: ')

#Chama a função para inverter a string
resultado = inverter_string(entrada)

print(f"String original: {entrada}")
print(f"String invertida: {resultado}")