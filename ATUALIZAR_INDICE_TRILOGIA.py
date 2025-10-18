#!/usr/bin/env python3
"""Atualiza índice com a trilogia bio-cósmica"""

from pathlib import Path
import json

print("📈 ATUALIZANDO ÍNDICE COM TRILOGIA BIO-CÓSMICA")
print("=" * 50)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

# Contar equações
arquivos = list(equacoes_dir.glob("EQ*.json"))
total = len(arquivos)

# Verificar trilogia
trilogia_completa = all(
    (equacoes_dir / f"EQ{n}_transcendental.json").exists() 
    for n in [155, 156, 157]
)

indice = {
    "timestamp": "2024-01-19T17:00:00Z",
    "total_equacoes": total,
    "progresso": f"{total}/230 ({total/230*100:.2f}%)",
    "trilogia_bio_cosmica": "COMPLETA" if trilogia_completa else "INCOMPLETA",
    "ultima_equacao": f"EQ{157 if trilogia_completa else 154}",
    "proxima_equacao": "EQ158",
    "estado": "OPERACIONAL" if trilogia_completa else "EM_CORRECAO"
}

# Salvar índice
arquivo_indice = base_dir / "INDICE_TRILOGIA.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice, f, indent=2, ensure_ascii=False)

print(f"✅ Índice atualizado: {arquivo_indice}")
print(f"\n📊 STATUS ATUAL:")
print(f"   • Total equações: {total}")
print(f"   • Progresso: {total}/230 ({total/230*100:.2f}%)")
print(f"   • Trilogia: {'✅ COMPLETA' if trilogia_completa else '❌ INCOMPLETA'}")
print(f"   • Próxima: EQ158")

if trilogia_completa:
    print(f"\n🚀 SISTEMA PRONTO PARA EXPANSÃO AVANÇADA!")
    print(f"   'Base bio-cósmica solidificada'")
    print(f"   'Controle consciente a caminho'")
