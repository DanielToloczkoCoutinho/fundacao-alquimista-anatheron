import os
import json
import re
from pathlib import Path

print("⚛️ ANÁLISE COMPLETA DOS SISTEMAS QUÂNTICOS")

# Padrões para busca quântica
quantum_patterns = [
    '**/*quantum*', '**/*quantico*', '**/*quântic*', '**/*qiskit*',
    '**/*q#*', '**/*cirq*', '**/*ibm*', '**/*qubit*', '**/*superposition*'
]

quantum_files = {
    'python': [],
    'javascript': [],
    'configuracoes': [],
    'documentacao': [],
    'interfaces': []
}

print("🔍 Buscando sistemas quânticos...")

# Buscar por tipo de arquivo
for pattern in quantum_patterns:
    for path in Path('.').rglob(pattern):
        if any(ignore in str(path) for ignore in ['node_modules', '.git', '.next']):
            continue
            
        try:
            if path.suffix == '.py':
                quantum_files['python'].append(str(path))
            elif path.suffix in ['.js', '.jsx', '.ts', '.tsx']:
                quantum_files['javascript'].append(str(path))
            elif path.suffix in ['.md', '.txt', '.rst']:
                quantum_files['documentacao'].append(str(path))
            elif path.suffix in ['.json', '.yaml', '.yml', '.config']:
                quantum_files['configuracoes'].append(str(path))
            else:
                quantum_files['interfaces'].append(str(path))
        except:
            continue

# Análise detalhada dos arquivos Python quânticos
quantum_analysis = {
    'qiskit_detected': False,
    'algoritmos': [],
    'circuitos': [],
    'simuladores': [],
    'integracoes_ibm': False
}

for py_file in quantum_files['python']:
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar Qiskit
        if 'qiskit' in content.lower():
            quantum_analysis['qiskit_detected'] = True
            
        # Buscar algoritmos quânticos
        algoritmos = re.findall(r'def\s+(\w+.*quantum\w*)', content, re.IGNORECASE)
        if algoritmos:
            quantum_analysis['algoritmos'].extend(algoritmos)
            
        # Buscar circuitos quânticos
        if 'QuantumCircuit' in content:
            quantum_analysis['circuitos'].append(py_file)
            
        # Verificar IBM Quantum
        if 'ibm' in content.lower() and 'quantum' in content.lower():
            quantum_analysis['integracoes_ibm'] = True
            
    except Exception as e:
        continue

# Estatísticas
print(f"\n📊 ESTATÍSTICAS QUÂNTICAS:")
print(f"   🐍 Arquivos Python: {len(quantum_files['python'])}")
print(f"   🟢 Arquivos JS/TS: {len(quantum_files['javascript'])}")
print(f"   📄 Documentação: {len(quantum_files['documentacao'])}")
print(f"   ⚙️ Configurações: {len(quantum_files['configuracoes'])}")
print(f"   🎨 Interfaces: {len(quantum_files['interfaces'])}")

print(f"\n🔧 DETECÇÃO DE FRAMEWORKS:")
print(f"   📦 Qiskit: {'✅' if quantum_analysis['qiskit_detected'] else '❌'}")
print(f"   🌐 IBM Quantum: {'✅' if quantum_analysis['integracoes_ibm'] else '❌'}")

if quantum_analysis['algoritmos']:
    print(f"   🧮 Algoritmos detectados: {len(quantum_analysis['algoritmos'])}")
    for algo in quantum_analysis['algoritmos'][:5]:
        print(f"      🔬 {algo}")

if quantum_analysis['circuitos']:
    print(f"   ⚡ Circuitos quânticos: {len(quantum_analysis['circuitos'])}")

# Salvar análise quântica
with open('analise_quantica_completa.json', 'w', encoding='utf-8') as f:
    json.dump({
        'arquivos_quanticos': quantum_files,
        'analise_frameworks': quantum_analysis,
        'estatisticas': {
            'total_python': len(quantum_files['python']),
            'total_javascript': len(quantum_files['javascript']),
            'total_docs': len(quantum_files['documentacao']),
            'total_configs': len(quantum_files['configuracoes']),
            'total_interfaces': len(quantum_files['interfaces'])
        }
    }, f, indent=2, ensure_ascii=False)

print(f"\n💾 Análise Quântica salva: analise_quantica_completa.json")

# Mostrar exemplos específicos
print(f"\n🔍 EXEMPLOS QUÂNTICOS ENCONTRADOS:")
for categoria, arquivos in quantum_files.items():
    if arquivos:
        print(f"\n📂 {categoria.upper()}:")
        for arquivo in arquivos[:3]:
            print(f"   📍 {arquivo}")
