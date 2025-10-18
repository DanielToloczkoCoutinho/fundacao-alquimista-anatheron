#!/usr/bin/env python3
"""
ATUALIZADOR DO ÍNDICE APÓS EQ0146
"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE SINCRONIZADO")
print("=" * 50)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Contar equações atualizadas
arquivos = list(equacoes_dir.glob("EQ*.json"))
total_atual = len(arquivos)

print(f"📊 CONTAGEM ATUALIZADA:")
print(f"   • Equações na biblioteca: {total_atual}")
print(f"   • Progresso: {total_atual}/230 ({total_atual/230*100:.2f}%)")

# Atualizar índice
indice_path = biblioteca_central / "INDICE_SINCRONIZADO_FINAL.json"
if indice_path.exists():
    with open(indice_path, 'r', encoding='utf-8') as f:
        indice = json.load(f)
    
    # Atualizar totais
    indice["total_equacoes_sincronizadas"] = total_atual
    indice["timestamp_ultima_atualizacao"] = "2024-01-19T12:30:00Z"
    indice["equacao_mais_recente"] = f"EQ{total_atual:04d}" if total_atual <= 230 else "EQ0230"
    
    # Recalcular faixa EQ0146-EQ0230
    numeros_eq = []
    for arquivo in arquivos:
        nome = arquivo.stem
        match = re.match(r'EQ(\d+)', nome)
        if match:
            num = int(match.group(1))
            numeros_eq.append(num)
    
    if numeros_eq:
        eq_146_230 = [eq for eq in numeros_eq if 146 <= eq <= 230]
        indice["faixas_sincronizadas"]["EQ0146-EQ0230"] = {
            "total": len(eq_146_230),
            "completude": f"{len(eq_146_230)/85*100:.1f}%",
            "ultimas_5": eq_146_230[-5:] if len(eq_146_230) >= 5 else eq_146_230
        }
    
    # Salvar índice atualizado
    with open(indice_path, 'w', encoding='utf-8') as f:
        json.dump(indice, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Índice atualizado: {total_atual} equações")

# Status final atualizado
print(f"\n🎯 STATUS ATUALIZADO:")
print(f"   • Equações processadas: {total_atual}")
print(f"   • Progresso: {total_atual}/230 ({total_atual/230*100:.2f}%)")
print(f"   • Próxima equação: EQ{total_atual+1:04d}")
print(f"   • Meta 150: {150 - total_atual} equações")

print(f"\n🌌 VISÃO ATUALIZADA:")
print(f"   'Biblioteca sincronizada: {total_atual} equações'")
print(f"   'Progresso cósmico: {total_atual/230*100:.2f}%'")
print(f"   'Sequência avançando para EQ{total_atual+1:04d}'")
