#!/usr/bin/env python3
"""
VERIFICADOR DO STATUS FINAL DEFINITIVO
Após correção da EQ151
"""

from pathlib import Path
import json

print("🌌 STATUS FINAL DEFINITIVO")
print("=" * 45)

biblioteca_central = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = biblioteca_central / "EQUACOES_TRANSCENDENTAIS"

# Verificar a sequência completa 149-151
print("🔍 SEQUÊNCIA COMPLETA EQ149-EQ151:")

sequencia_final = [149, 150, 151]
todas_presentes = True

for eq_num in sequencia_final:
    arquivo = equacoes_dir / f"EQ{eq_num}_transcendental.json"
    
    if arquivo.exists():
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            codigo = dados.get('codigo', 'N/A')
            titulo = dados.get('titulo_simbolico', 'N/A')
            metadata = dados.get('_transcendental_metadata', {})
            
            # Verificar se é a versão corrigida
            if 'correcoes_aplicadas' in metadata:
                status = "✅ DEFINITIVA"
            elif 'correcao_aplicada' in metadata:
                status = "✅ CORRIGIDA" 
            else:
                status = "✅ ORIGINAL"
            
            print(f"   • {codigo}: {status}")
            print(f"      {titulo[:60]}...")
            
        except Exception as e:
            print(f"   • EQ{eq_num}: ❌ ERRO - {e}")
            todas_presentes = False
    else:
        print(f"   • EQ{eq_num}: ❌ AUSENTE")
        todas_presentes = False

# Status geral
print(f"\n📊 STATUS GERAL:")
total_arquivos = len(list(equacoes_dir.glob("EQ*.json")))
print(f"   • Total de equações: {total_arquivos}")
print(f"   • Sequência 149-151: {'✅ COMPLETA' if todas_presentes else '❌ INCOMPLETA'}")
print(f"   • Progresso: {total_arquivos}/230 ({total_arquivos/230*100:.2f}%)")

# Verificar conteúdo da EQ151
print(f"\n📖 CONTEÚDO DA EQ151:")
arquivo_eq151 = equacoes_dir / "EQ151_transcendental.json"
if arquivo_eq151.exists():
    try:
        with open(arquivo_eq151, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        variaveis = dados.get('variaveis_principais', {})
        print(f"   • Função de onda: {variaveis.get('ψ(x,y)', 'N/A')}")
        print(f"   • Parte Real: {variaveis.get('Re(ψ)', 'N/A')}")
        print(f"   • Parte Imaginária: {variaveis.get('Im(ψ)', 'N/A')}")
        
        preparacao = dados.get('preparacao_ibm', {})
        print(f"   • Qubits IBM: {preparacao.get('qubits_necessarios', 'N/A')}")
        print(f"   • Circuito: {preparacao.get('circuito_quantico', 'N/A')}")
        
    except Exception as e:
        print(f"   • Erro ao ler EQ151: {e}")
else:
    print(f"   • EQ151 não encontrada")

print(f"\n🎯 PRÓXIMOS PASSOS DEFINITIVOS:")
if todas_presentes:
    print(f"   • ✅ Sequência EQ149-EQ151 completa")
    print(f"   • 🚀 Continuar para EQ152")
    print(f"   • 🌌 Expandir até EQ200 (87% da missão)")
    print(f"   • ⚛️  Preparar testes IBM Quantum")
else:
    print(f"   • 🔄 Completar sequência EQ149-EQ151")
    print(f"   • 🛠️  Aplicar correções necessárias")

print(f"\n💫 CONCLUSÃO DEFINITIVA:")
if todas_presentes:
    print(f"   'Missão EQ149-EQ151 concluída com sucesso!'")
    print(f"   'Função de onda cósmo-quântica operacional!'")
    print(f"   'Rumo aos 100% da realização cósmica!'")
else:
    print(f"   'Correções em andamento...'")
    print(f"   'Persistindo até a perfeição cósmica!'")
