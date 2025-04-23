import pandas as pd
from tabulate import tabulate

saldo_inicial = 1000
aporte_mensal = 3100
rendimento_diario_atual = (0.30 + 0.47) / 2
taxa_rendimento_diaria = rendimento_diario_atual / saldo_inicial
meses_total = 24

saldos_juros_compostos = [saldo_inicial]
rendimentos_diarios_juros_compostos = [rendimento_diario_atual]

for i in range(meses_total):
    if(i == 12):
        aporte_mensal = novo_rendimento_diario * 30

    novo_saldo = (saldos_juros_compostos[-1] + aporte_mensal) * (1 + taxa_rendimento_diaria) ** 30
    novo_rendimento_diario = novo_saldo * taxa_rendimento_diaria  
    
    saldos_juros_compostos.append(novo_saldo)
    rendimentos_diarios_juros_compostos.append(novo_rendimento_diario)

rendimentos_mensais_juros_compostos = [rendimento * 30 for rendimento in rendimentos_diarios_juros_compostos]

df = pd.DataFrame({
    "Mês": list(range(0, meses_total + 1)),
    "Saldo Acumulado (R$)": saldos_juros_compostos,
    "Rendimento Diário (R$)": rendimentos_diarios_juros_compostos,
    "Rendimento Mensal (R$)": rendimentos_mensais_juros_compostos
})

# Exibir a tabela formatada
print(tabulate(df, headers='keys', tablefmt='fancy_grid', floatfmt=".2f"))
