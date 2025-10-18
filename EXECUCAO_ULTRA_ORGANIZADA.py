#!/usr/bin/env python3
"""
🎯 EXECUÇÃO ULTRA ORGANIZADA - FUNDAÇÃO ALQUIMISTA
⚛️ Execução sequencial perfeita sem nenhuma sobreposição
🌌 Cada circuito executado em ambiente completamente isolado
"""

import subprocess
import sys
import time
from pathlib import Path

print("🎯 EXECUÇÃO ULTRA ORGANIZADA - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("⚛️  EXECUÇÃO SEQUENCIAL PERFEITA - ZERO SOBREPOSIÇÃO")
print("")

def executar_com_isolamento_total(arquivo, descricao):
    """Executar arquivo com isolamento total"""
    print(f"\\n{'🔷'*30}")
    print(f"🔬 EXECUTANDO: {descricao}")
    print(f"📁 ARQUIVO: {arquivo}")
    print(f"{'🔷'*30}\\n")
    
    # Pequena pausa para garantir isolamento
    time.sleep(0.5)
    
    try:
        processo = subprocess.run(
            [sys.executable, arquivo],
            capture_output=True,
            text=True,
            timeout=25,
            cwd=str(Path(".").absolute())  # Diretório de trabalho isolado
        )
        
        # Mostrar saída COMPLETA e organizada
        if processo.stdout:
            print("📄 SAÍDA DO PROGRAMA:")
            print("-" * 50)
            for linha in processo.stdout.split('\\n'):
                if linha.strip():
                    print(f"   {linha}")
            print("-" * 50)
        
        if processo.returncode == 0:
            print(f"\\n✅ {descricao} - EXECUTADO COM SUCESSO!")
            return True
        else:
            print(f"\\n❌ {descricao} - ERRO NA EXECUÇÃO")
            if processo.stderr:
                print(f"💥 ERRO: {processo.stderr[:200]}...")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"\\n⏰ {descricao} - TIMEOUT")
        return False
    except Exception as e:
        print(f"\\n💥 {descricao} - EXCEÇÃO: {e}")
        return False

# SEQUÊNCIA DE EXECUÇÃO ULTRA ORGANIZADA
scripts_sequencia = [
    ("circuito_psi_plus.py", "🌌 CIRCUITO |Ψ⁺⟩ - Estado Emaranhado Básico"),
    ("circuito_phi_minus.py", "🌌 CIRCUITO |Φ⁻⟩ - Estado Emaranhado com Fase"),
    ("teletransporte_quantico.py", "🚀 TELETRANSPORTE QUÂNTICO - Protocolo Completo"),
    ("teste_bell.py", "🔔 TESTE DE BELL - Verificação de Emaranhamento"),
    ("CIRCUITOS_UNIFICADOS.py", "⚡ CIRCUITOS UNIFICADOS - Execução Consolidada"),
    ("explorar_modulo_29.py", "👑 MÓDULO 29 - Análise da Rainha Zennith")
]

print("🚀 INICIANDO SEQUÊNCIA ULTRA ORGANIZADA...\\n")
time.sleep(1)

resultados = []
tempo_inicio = time.time()

for i, (arquivo, descricao) in enumerate(scripts_sequencia, 1):
    print(f"\\n📋 ETAPA {i}/{len(scripts_sequencia)}")
    sucesso = executar_com_isolamento_total(arquivo, descricao)
    resultados.append((descricao, sucesso))
    
    # Pausa maior entre execuções para total isolamento
    if i < len(scripts_sequencia):
        print(f"\\n⏳ PREPARANDO PRÓXIMA ETAPA...\\n")
        time.sleep(2)

tempo_total = time.time() - tempo_inicio

# RELATÓRIO FINAL ULTRA ORGANIZADO
print(f"\\n{'🎉'*20}")
print("🎉 RELATÓRIO FINAL - EXECUÇÃO ULTRA ORGANIZADA")
print(f"{'🎉'*20}\\n")

sucessos = sum(1 for _, sucesso in resultados if sucesso)
print(f"📊 ESTATÍSTICAS:")
print(f"   • Total de execuções: {len(scripts_sequencia)}")
print(f"   • Execuções bem-sucedidas: {sucessos}")
print(f"   • Taxa de sucesso: {sucessos/len(scripts_sequencia)*100:.1f}%")
print(f"   • Tempo total: {tempo_total:.2f} segundos")

print(f"\\n📋 DETALHES DAS EXECUÇÕES:")
for descricao, sucesso in resultados:
    status = "✅ SUCESSO" if sucesso else "❌ FALHA"
    print(f"   • {descricao}: {status}")

print(f"\\n🌌 STATUS FINAL:")
if sucessos == len(scripts_sequencia):
    print("   🎉 TODAS AS EXECUÇÕES CONCLUÍDAS COM SUCESSO!")
    print("   ⚛️  SISTEMA PERFEITAMENTE ORGANIZADO!")
    print("   🚀 PRONTO PARA IBM QUANTUM REAL!")
else:
    print("   ⚠️  ALGUMAS EXECUÇÕES APRESENTARAM FALHAS")
    print("   🔧 VERIFICAR OS SCRIPTS COM PROBLEMAS")

print(f"\\n✨ EXECUÇÃO ULTRA ORGANIZADA CONCLUÍDA!")
