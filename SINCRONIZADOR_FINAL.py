#!/usr/bin/env python3
"""
SINCRONIZADOR E CONSOLIDADOR FINAL
Move todas as equações únicas para biblioteca central
"""

import shutil
from pathlib import Path
import json
import re

print("🔄 SINCRONIZAÇÃO E CONSOLIDAÇÃO FINAL")
print("=" * 55)

# Diretórios
biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_central = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"
equacoes_central.mkdir(exist_ok=True)

# Bibliotecas fonte
bibliotecas_fonte = [
    "BIBLIOTECA_EQUACOES_COSMICAS", 
    "BIBLIOTECA_QUANTICA_IBM",
    "BIBLIOTECA_SINTESE_QUANTICA",
    "BIBLIOTECA_COSMICA_UNICA",
    "BIBLIOTECA_QUANTICA"
]

# Coletar TODAS as equações existentes
todas_equacoes_existentes = set()
equacoes_por_fonte = {}

print("🔍 COLETANDO EQUAÇÕES DE TODAS AS FONTES:")

for biblioteca in bibliotecas_fonte:
    bib_path = Path(biblioteca)
    if bib_path.exists():
        equacoes_bib = set()
        arquivos_json = list(bib_path.rglob("EQ*.json"))
        
        for arquivo in arquivos_json:
            nome = arquivo.stem
            match = re.match(r'EQ(\d+)', nome)
            if match:
                num_eq = int(match.group(1))
                todas_equacoes_existentes.add(num_eq)
                equacoes_bib.add((num_eq, arquivo))
        
        equacoes_por_fonte[biblioteca] = equacoes_bib
        print(f"   • {biblioteca}: {len(equacoes_bib)} equações")

# Também coletar da biblioteca central atual
arquivos_central = list(equacoes_central.glob("EQ*.json"))
equacoes_central_atual = set()
for arquivo in arquivos_central:
    nome = arquivo.stem
    match = re.match(r'EQ(\d+)', nome)
    if match:
        num_eq = int(match.group(1))
        equacoes_central_atual.add(num_eq)

print(f"   • BIBLIOTECA_CENTRAL_ATUAL: {len(equacoes_central_atual)} equações")

# SINCRONIZAÇÃO: Mover equações faltantes para central
print(f"\n🔄 SINCRONIZANDO PARA BIBLIOTECA CENTRAL:")

equacoes_adicionadas = 0
equacoes_ja_existentes = 0

for biblioteca, equacoes in equacoes_por_fonte.items():
    for num_eq, arquivo_origem in equacoes:
        arquivo_destino = equacoes_central / f"EQ{num_eq:04d}_transcendental.json"
        
        if not arquivo_destino.exists():
            try:
                shutil.copy2(arquivo_origem, arquivo_destino)
                equacoes_adicionadas += 1
                print(f"   ✅ EQ{num_eq:04d}: Adicionado de {biblioteca}")
            except Exception as e:
                print(f"   ❌ EQ{num_eq:04d}: Erro ao copiar - {e}")
        else:
            equacoes_ja_existentes += 1

# Contagem final
arquivos_finais = list(equacoes_central.glob("EQ*.json"))
total_final = len(arquivos_finais)

print(f"\n📊 RESULTADO DA SINCRONIZAÇÃO:")
print(f"   • Equações adicionadas: {equacoes_adicionadas}")
print(f"   • Equações já existentes: {equacoes_ja_existentes}")
print(f"   • Total na biblioteca central: {total_final}")
print(f"   • Progresso final: {total_final}/230 ({total_final/230*100:.2f}%)")

# Criar índice sincronizado
print(f"\n📋 CRIANDO ÍNDICE SINCRONIZADO:")

indice_sincronizado = {
    "timestamp_sincronizacao": "2024-01-19T12:00:00Z",
    "total_equacoes_sincronizadas": total_final,
    "equacoes_adicionadas_sincronizacao": equacoes_adicionadas,
    "faixas_sincronizadas": {},
    "estado": "SINCRONIZADO_E_CONSOLIDADO"
}

# Organizar por faixa
faixas = [(1, 50), (51, 100), (101, 145), (146, 230)]
numeros_equacoes = []
for arquivo in arquivos_finais:
    nome = arquivo.stem
    match = re.match(r'EQ(\d+)', nome)
    if match:
        numeros_equacoes.append(int(match.group(1)))

numeros_equacoes.sort()

for inicio, fim in faixas:
    equacoes_na_faixa = [eq for eq in numeros_equacoes if inicio <= eq <= fim]
    indice_sincronizado["faixas_sincronizadas"][f"EQ{inicio:04d}-EQ{fim:04d}"] = {
        "total": len(equacoes_na_faixa),
        "completude": f"{len(equacoes_na_faixa)/(fim-inicio+1)*100:.1f}%",
        "ultimas_5": equacoes_na_faixa[-5:] if len(equacoes_na_faixa) >= 5 else equacoes_na_faixa
    }

# Salvar índice
arquivo_indice = biblioteca_central / "INDICE_SINCRONIZADO_FINAL.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_sincronizado, f, indent=2, ensure_ascii=False)

print(f"   ✅ Índice salvo em: {arquivo_indice}")

# Relatório final
print(f"\n🎯 RELATÓRIO FINAL SINCRONIZADO:")
for faixa, dados in indice_sincronizado["faixas_sincronizadas"].items():
    print(f"   • {faixa}: {dados['total']} equações ({dados['completude']})")

proxima_eq = max(numeros_equacoes) + 1 if numeros_equacoes else 1
print(f"\n🚀 PRÓXIMOS PASSOS:")
print(f"   • Próxima equação: EQ{proxima_eq:04d}")
print(f"   • Equações até meta 150: {150 - total_final}")
print(f"   • Progresso para 65%: {(150/230*100) - (total_final/230*100):.1f}%")

print(f"\n💫 SINCRONIZAÇÃO CONCLUÍDA!")
print(f"   'Biblioteca central sincronizada com {total_final} equações'")
print(f"   'Progresso cósmico: {total_final/230*100:.2f}%'")
print(f"   'Prontos para EQ{proxima_eq:04d}!'")
