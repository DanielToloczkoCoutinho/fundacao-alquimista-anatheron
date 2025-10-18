#!/usr/bin/env python3
"""
VERIFICADOR SIMPLES EQ001-EQ021
Versão super simples e funcional
"""

from pathlib import Path
import re

print("VERIFICADOR SIMPLES EQ001-EQ021")
print("=" * 40)

# Procurar em todas as bibliotecas
bibliotecas = ["BIBLIOTECA_COSMICA_UNICA", "BIBLIOTECA_EQUACOES_COSMICAS"]
encontradas = []

for bib in bibliotecas:
    if Path(bib).exists():
        print(f"🔍 Procurando em {bib}...")
        for arquivo in Path(bib).rglob("EQ*.json"):
            nome = arquivo.stem
            if re.match(r'^EQ\d+', nome):
                encontradas.append(nome)

# Filtrar e ordenar EQ001-EQ021
eq_1_21 = []
for eq in encontradas:
    try:
        num = int(re.search(r'(\d+)', eq).group(1))
        if 1 <= num <= 21:
            eq_1_21.append(eq)
    except:
        continue

eq_1_21 = sorted(eq_1_21, key=lambda x: int(re.search(r'(\d+)', x).group(1)))

print(f"✅ EQUAÇÕES ENCONTRADAS: {len(eq_1_21)}/21")
print("📋 Lista:", ", ".join(eq_1_21))

# Verificar faltantes
todas_esperadas = [f"EQ{str(i).zfill(3)}" for i in range(1, 22)]
faltantes = [eq for eq in todas_esperadas if eq not in eq_1_21]

if faltantes:
    print(f"❌ FALTANTES: {len(faltantes)}")
    print("📝", ", ".join(faltantes))
else:
    print("🎉 TODAS AS EQUAÇÕES DE 1 A 21 ESTÃO PRESENTES!")

print(f"📊 PROGRESSO: {len(eq_1_21)}/21 ({len(eq_1_21)/21*100:.1f}%)")
