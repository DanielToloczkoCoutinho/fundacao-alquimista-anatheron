#!/usr/bin/env python3
"""
🔍 VERIFICADOR DE SINTÁXE PREVENTIVO
⚡ Verifica scripts Python antes da execução
🛡️ Previne erros de caracteres especiais
"""

import ast
import sys
from pathlib import Path

print("🔍 VERIFICADOR DE SINTÁXE PREVENTIVO")
print("=" * 50)

def verificar_sintaxe_arquivo(caminho_arquivo):
    """Verificar sintaxe de um arquivo Python"""
    print(f"📁 Verificando: {caminho_arquivo}")
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        # Tentar compilar para verificar sintaxe
        ast.parse(codigo)
        print("   ✅ Sintaxe OK")
        return True
        
    except SyntaxError as e:
        print(f"   ❌ ERRO DE SINTAXE:")
        print(f"      Linha {e.lineno}: {e.msg}")
        print(f"      {e.text}")
        return False
    except Exception as e:
        print(f"   ⚠️  Outro erro: {e}")
        return False

# Verificar todos os scripts recentes
scripts_para_verificar = [
    "PROCESSADOR_EQUACOES_COSMICAS_2.py",
    "CATALOGADOR_EQUACOES_COSMICAS.py", 
    "PESQUISADOR_EQUACOES_GLOBAL.py",
    "VERIFICADOR_TEMPO_REAL.py"
]

print("\n🔧 VERIFICANDO TODOS OS SCRIPTS...")
for script in scripts_para_verificar:
    if Path(script).exists():
        verificar_sintaxe_arquivo(script)
    else:
        print(f"   📭 {script} não encontrado")

print("\n🎯 VERIFICAÇÃO CONCLUÍDA!")
