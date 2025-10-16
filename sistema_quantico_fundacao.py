#!/usr/bin/env python3
"""
🌌 SISTEMA QUÂNTICO DA FUNDAÇÃO ALQUIMISTA
Solução independente de ambiente virtual
"""

import subprocess
import sys
import os

def check_install(package):
    """Verificar se pacote está instalado"""
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def install_package(package):
    """Instalar pacote usando pip do usuário"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🌌 INICIANDO SISTEMA QUÂNTICO DA FUNDAÇÃO")
    print("🔍 Verificando dependências...")
    
    # Verificar dependências críticas
    dependencies = ['numpy', 'scipy', 'qiskit']
    missing = []
    
    for dep in dependencies:
        if check_install(dep):
            print(f"✅ {dep} instalado")
        else:
            print(f"❌ {dep} faltando")
            missing.append(dep)
    
    if missing:
        print(f"\n📦 Instalando dependências faltantes: {missing}")
        for dep in missing:
            print(f"🔧 Instalando {dep}...")
            if install_package(dep):
                print(f"✅ {dep} instalado com sucesso!")
            else:
                print(f"❌ Falha ao instalar {dep}")
                return False
    
    # Executar sistema quântico
    print("\n🚀 EXECUTANDO SISTEMA QUÂNTICO...")
    try:
        from qiskit import QuantumCircuit, Aer, transpile
        import numpy as np
        
        print("🌌 CRIANDO CIRCUITO QUÂNTICO AVANÇADO")
        
        # Circuito de demonstração
        qc = QuantumCircuit(3, 3)
        qc.h(0)  # Porta Hadamard - superposição
        qc.cx(0, 1)  # CNOT - emaranhamento
        qc.cx(1, 2)  # CNOT - cadeia de emaranhamento
        qc.measure_all()
        
        print("🔮 Circuito Criado:")
        print(qc)
        
        # Simular
        simulator = Aer.get_backend('aer_simulator')
        result = simulator.run(qc, shots=1000).result()
        counts = result.get_counts()
        
        print("\n📊 RESULTADOS DA SIMULAÇÃO:")
        print("=" * 40)
        for state, count in sorted(counts.items()):
            probability = (count / 1000) * 100
            print(f"   {state}: {count:3d} execuções ({probability:5.1f}%)")
        
        # Análise dos resultados
        total = sum(counts.values())
        entangled_states = ['000', '111']  # Estados emaranhados
        entangled_count = sum(counts.get(state, 0) for state in entangled_states)
        entanglement_ratio = (entangled_count / total) * 100
        
        print(f"\n🔗 ANÁLISE DE EMPARELHAMENTO:")
        print(f"   Estados emaranhados: {entangled_states}")
        print(f"   Taxa de emaranhamento: {entanglement_ratio:.1f}%")
        
        print("\n✅ SISTEMA QUÂNTICO OPERACIONAL!")
        print("🎯 Fundação Alquimista pronta para computação quântica!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na execução quântica: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
