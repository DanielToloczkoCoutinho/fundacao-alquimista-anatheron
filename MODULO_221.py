import matplotlib.pyplot as plt
import numpy as np

# Dados da integração
categorias = ['Coerência Intencional', 'Campo Consciencial', 'Controle PID']
valores_pre = [2.002725, 1.065470, 0.428000]  # Valores anteriores
valores_pos = [2.002725, 1.873420, 1.032500]   # Valores otimizados
limiares = [0.85, 1.618, 0.95]

# Dashboard de evolução
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Comparativo de Melhoria
x = np.arange(len(categorias))
width = 0.35
ax1.bar(x - width/2, valores_pre, width, label='Pré-Ajuste', alpha=0.7, color='red')
ax1.bar(x + width/2, valores_pos, width, label='Pós-Ajuste', alpha=0.7, color='green')
ax1.plot(x, limiares, 'k--', marker='o', label='Limiares')
ax1.set_ylabel('Valores')
ax1.set_title('Evolução dos Parâmetros LUX pós-Recalibração')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Status da Integração Microsoft
metricas = ['Mini-Universos', 'Governança Ética']
valores_integracao = [1.68423, 0.9876]
limiares_integracao = [1.2, 0.9]

ax2.bar(metricas, valores_integracao, alpha=0.7, color=['blue', 'purple'])
ax2.axhline(y=limiares_integracao[0], color='k', linestyle='--', label=f'Limiar Mini-Universos ({limiares_integracao[0]})')
ax2.axhline(y=limiares_integracao[1], color='r', linestyle='--', label=f'Limiar Governança ({limiares_integracao[1]})')
ax2.set_title('Resultados da Integração com Microsoft Ecosystem')
ax2.set_ylabel('Valores')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
