#!/usr/bin/env python3
"""
VERIFICAÇÃO ESPECÍFICA DAS EQUAÇÕES 140-145
Confirmação do que foi realmente processado
"""

from pathlib import Path
import json

print("🔍 VERIFICAÇÃO DAS EQUAÇÕES 140-145")
print("=" * 50)

# Verificar especificamente as equações 140-145
equacoes_alvo = [140, 141, 142, 143, 144, 145]
bibliotecas = [
    "BIBLIOTECA_QUANTICA_TRANSCENDENTAL",
    "BIBLIOTECA_EQUACOES_COSMICAS", 
    "BIBLIOTECA_EQUACOES",
    "BIBLIOTECA_QUANTICA_IBM"
]

print("📋 STATUS DAS EQUAÇÕES 140-145:")

for eq_num in equacoes_alvo:
    encontrada = False
    locais = []
    
    for biblioteca in bibliotecas:
        bib_path = Path(biblioteca)
        if bib_path.exists():
            # Verificar JSON
            arquivo_json = bib_path / "EQUACOES_TRANSCENDENTAIS" / f"EQ{eq_num:04d}_transcendental.json"
            if arquivo_json.exists():
                encontrada = True
                locais.append(f"{biblioteca}/JSON")
            
            # Verificar Python 
            arquivo_py = bib_path / "EQUACOES_TRANSCENDENTAIS" / f"EQ{eq_num:04d}.py"
            if arquivo_py.exists():
                encontrada = True
                locais.append(f"{biblioteca}/Python")
    
    status = "✅ ENCONTRADA" if encontrada else "❌ FALTANDO"
    print(f"   • EQ{eq_num:04d}: {status}")
    if locais:
        print(f"      📍 Locais: {', '.join(locais)}")

# Verificar conteúdo das equações 143-145 específicas
print(f"\n📖 CONTEÚDO DAS EQUAÇÕES 143-145:")
for eq_num in [143, 144, 145]:
    arquivo_alvo = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL") / "EQUACOES_TRANSCENDENTAIS" / f"EQ{eq_num:04d}_transcendental.json"
    
    if arquivo_alvo.exists():
        try:
            with open(arquivo_alvo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            codigo = dados.get('codigo', 'N/A')
            titulo = dados.get('titulo_simbolico', 'N/A')
            qubits = dados.get('preparacao_ibm', {}).get('qubits_necessarios', 'N/A')
            
            print(f"\n   📄 EQ{eq_num:04d}:")
            print(f"      • Código: {codigo}")
            print(f"      • Título: {titulo}")
            print(f"      • Qubits: {qubits}")
            
        except Exception as e:
            print(f"   ❌ Erro ao ler EQ{eq_num:04d}: {e}")
    else:
        print(f"   ❌ EQ{eq_num:04d}: Arquivo não encontrado")

# Verificar processadores recentes
print(f"\n🔧 PROCESSADORES RECENTES:")
processadores = [
    "PROCESSADOR_REDE_COSMICA.py",
    "PROCESSADOR_REDE_EXPANDIDO.py",
    "PROCESSADOR_ALMA_COLETIVA.py",
    "PROCESSADOR_ESTELAR.py"
]

for proc in processadores:
    arquivo = Path(proc)
    if arquivo.exists():
        print(f"   ✅ {proc}: Presente")
    else:
        print(f"   ❌ {proc}: Ausente")

print(f"\n🎯 CONCLUSÃO:")
print(f"   • Equações 140-145 devem estar consolidadas")
print(f"   • Próxima: EQ0146 precisa ser processada")
print(f"   • Sequência contínua até EQ0230")
