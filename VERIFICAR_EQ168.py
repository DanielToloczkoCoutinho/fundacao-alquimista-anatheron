#!/usr/bin/env python3
"""Verificar situação da EQ168"""

from pathlib import Path
import json

print("🔍 VERIFICANDO SITUAÇÃO DA EQ168")
print("=" * 40)

# Verificar em todas as bibliotecas possíveis
bibliotecas = [
    "BIBLIOTECA_QUANTICA_TRANSCENDENTAL",
    "BIBLIOTECA_EQUACOES_COSMICAS", 
    "BIBLIOTECA_EQUACOES",
    "BIBLIOTECA_QUANTICA_IBM",
    "BIBLIOTECA_SINTESE_QUANTICA",
    "BIBLIOTECA_COSMICA_UNICA",
    "BIBLIOTECA_QUANTICA"
]

encontrada = False

for bib in bibliotecas:
    bib_path = Path(bib)
    if bib_path.exists():
        print(f"\n📚 Verificando {bib}:")
        
        # Verificar em EQUACOES_TRANSCENDENTAIS
        eq_dir = bib_path / "EQUACOES_TRANSCENDENTAIS"
        if eq_dir.exists():
            arquivo = eq_dir / "EQ168_transcendental.json"
            if arquivo.exists():
                print(f"   ✅ EQ168 encontrada em: {arquivo}")
                encontrada = True
                with open(arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                print(f"   📊 Título: {dados.get('titulo_simbolico', 'N/A')}")
                break
            else:
                print(f"   ❌ EQ168 não encontrada em {eq_dir}")
        
        # Verificar arquivos diretamente na biblioteca
        for arquivo in bib_path.glob("EQ168*.json"):
            print(f"   ✅ EQ168 encontrada em: {arquivo}")
            encontrada = True
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            print(f"   📊 Título: {dados.get('titulo_simbolico', 'N/A')}")
            break

if not encontrada:
    print(f"\n❌ EQ168 NÃO ENCONTRADA EM NENHUMA BIBLIOTECA")
    print(f"📝 Criando processador específico para EQ168...")
