import re
import os

equacoes = {}
for file in open('equacoes_encontradas.txt').readlines():
    file = file.strip()
    if os.path.exists(file):
        content = open(file).read()
        matches = re.findall(r'EQ(\d+)', content)
        for eq in matches:
            equacoes[int(eq)] = file

# Ordenar e salvar
with open('equacoes_organizadas.txt', 'w') as f:
    for eq_num in sorted(equacoes.keys()):
        f.write(f"EQ{eq_num:03d}: {equacoes[eq_num]}\n")

print(f"📐 Equações organizadas: {len(equacoes)} encontradas")
