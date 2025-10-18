#!/usr/bin/env python3
"""Verificador simples da trilogia bio-cósmica"""

from pathlib import Path
import json

print("🔍 VERIFICANDO TRILOGIA BIO-CÓSMICA")
print("=" * 40)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

trilogia = [155, 156, 157]
encontradas = []

for num in trilogia:
    arquivo = equacoes_dir / f"EQ{num}_transcendental.json"
    if arquivo.exists():
        encontradas.append(num)
        print(f"✅ EQ{num} - PRESENTE")
    else:
        print(f"❌ EQ{num} - AUSENTE")

print(f"\n📊 RESULTADO:")
print(f"   • Encontradas: {len(encontradas)}/3")
print(f"   • Status: {'COMPLETA' if len(encontradas) == 3 else 'INCOMPLETA'}")

if len(encontradas) == 3:
    print(f"\n🎉 TRILOGIA BIO-CÓSMICA COMPLETA!")
    print(f"   EQ155 → EQ156 → EQ157 → OPERACIONAL")
else:
    print(f"\n⚠️  Faltantes: {[f'EQ{n}' for n in trilogia if n not in encontradas]}")
