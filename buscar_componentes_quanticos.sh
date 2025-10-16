#!/bin/bash

echo "🔍 BUSCA AVANÇADA POR COMPONENTES QUÂNTICOS"

# Componentes React quânticos
echo ""
echo "⚛️ COMPONENTES REACT QUÂNTICOS:"
find src -name "*.tsx" -o -name "*.jsx" | xargs grep -l "quantum\|quântic\|qiskit\|qubit" 2>/dev/null | head -10

# Scripts Python quânticos
echo ""
echo "🐍 SCRIPTS PYTHON QUÂNTICOS:"
find . -name "*.py" | xargs grep -l "quantum\|qiskit\|QuantumCircuit" 2>/dev/null | head -10

# Configurações quânticas
echo ""
echo "⚙️ CONFIGURAÇÕES QUÂNTICAS:"
find . -name "*.json" -o -name "*.yaml" -o -name "*.yml" | xargs grep -l "quantum\|qiskit\|ibm" 2>/dev/null | head -10

# Documentação quântica
echo ""
echo "📚 DOCUMENTAÇÃO QUÂNTICA:"
find . -name "*.md" | xargs grep -l "quantum\|quântic\|qiskit" 2>/dev/null | head -10

# Verificar se há integração com IBM Quantum
echo ""
echo "🌐 VERIFICANDO IBM QUANTUM:"
find . -type f -exec grep -l "ibm_quantum\|ibmq\|quantum-computing.ibm.com" {} \; 2>/dev/null

# Verificar algoritmos quânticos
echo ""
echo "🧮 ALGORITMOS QUÂNTICOS:"
find . -name "*.py" -exec grep -l "def.*quantum\|class.*Quantum" {} \; 2>/dev/null
