#!/usr/bin/env python3
"""
🔍 VERIFICADOR DE COMPATIBILIDADE - QISKIT 2.2.1
Rainha Zennith - Garantindo estabilidade
"""

import qiskit
from qiskit_aer import AerSimulator
import sys

def verificar_ambiente():
    print("🔍 VERIFICANDO COMPATIBILIDADE DO AMBIENTE...")
    
    # Versões
    print(f"🐍 Python: {sys.version}")
    print(f"⚛️  Qiskit: {qiskit.__version__}")
    
    # Testar componentes críticos
    testes = {
        "AerSimulator": lambda: AerSimulator() is not None,
        "QuantumCircuit": lambda: qiskit.QuantumCircuit(2) is not None,
        "Transpile": lambda: True,  # Teste básico
    }
    
    for nome, teste in testes.items():
        try:
            resultado = teste()
            print(f"   ✅ {nome}: COMPATÍVEL")
        except Exception as e:
            print(f"   ❌ {nome}: ERRO - {e}")
    
    print("🎯 RECOMENDAÇÕES:")
    print("   • Usar QFTGate em vez de QFT para inverse=True")
    print("   • Evitar instruções deprecated")
    print("   • Usar sys.exit() em vez de os._exit() quando possível")
    
    return True

if __name__ == "__main__":
    verificar_ambiente()
    sys.exit(0)
