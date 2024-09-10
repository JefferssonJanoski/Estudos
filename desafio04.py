#Dados de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#Calcula o faturamento total
faturamento_total = sum(faturamento.values())

percentuais = {
    estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()
}

print('Percentual de representação de cada estado:')
for estado, percentual in percentuais.items():
    print('{}: {:.2f}%'.format(estado, percentual))
