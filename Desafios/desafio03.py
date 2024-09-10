import json

def calcular_faturamento(faturamentos):

    faturamentos_validos = [(i, f) for i, f in enumerate(faturamentos) if f > 0]
    dia_menor_faturamento, menor_faturamento = min(faturamentos_validos, key=lambda x: x[1])
    dia_maior_faturamento, maior_faturamento = max(faturamentos_validos, key=lambda x: x[1])
    
    media_mensal = sum(f for _, f in faturamentos_validos) / len(faturamentos_validos)
    
    dias_acima_da_media = len([f for _, f in faturamentos_validos if f > media_mensal])
    
    return dia_menor_faturamento, menor_faturamento, dia_maior_faturamento, maior_faturamento, dias_acima_da_media

def main():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    faturamentos = dados['faturamento_diario']
    
    dia_menor, menor, dia_maior, maior, dias_acima_media = calcular_faturamento(faturamentos)

    print('No dia {} tivemos o menor faturamento: R${:.2f}'.format(dia_menor+1, menor))
    print('No dia {} tivemos o maior faturamento: R${:.2f}'.format(dia_maior+1, maior))
    print('Quantidade de dias que faturamos acima da média:', dias_acima_media)

if __name__ == '__main__':
    main()