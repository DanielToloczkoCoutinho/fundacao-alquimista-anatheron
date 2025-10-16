#!/bin/bash

echo "🔍 BUSCA OTIMIZADA POR COMPONENTES QUÂNTICOS"
echo "🎯 Focando nos arquivos mais relevantes..."

# Buscar apenas nos diretórios principais
DIRETORIOS_PRINCIPAIS=("src" "docs" "SCRIPTS_CENTRALIZADOS" ".")

for dir in "${DIRETORIOS_PRINCIPAIS[@]}"; do
    if [ -d "$dir" ]; then
        echo ""
        echo "📂 BUSCANDO EM: $dir"
        
        # Componentes React quânticos
        find "$dir" -maxdepth 3 -name "*.tsx" -o -name "*.jsx" | head -5 | while read file; do
            if grep -q -i "quantum\|quântic\|qiskit\|qubit" "$file" 2>/dev/null; then
                echo "⚛️  React: $file"
            fi
        done
        
        # Scripts Python quânticos
        find "$dir" -maxdepth 3 -name "*.py" | head -5 | while read file; do
            if grep -q -i "quantum\|qiskit\|QuantumCircuit" "$file" 2>/dev/null; then
                echo "🐍 Python: $file"
            fi
        done
    fi
done

echo ""
echo "🌐 VERIFICANDO IBM QUANTUM (RÁPIDO):"
find . -name "*ibm*quantum*" -o -name "*qiskit*" 2>/dev/null | head -5

echo ""
echo "📊 RESUMO DOS COMPONENTES ENCONTRADOS:"
echo "   ⚛️  Componentes React: $(find src -name "*.tsx" -o -name "*.jsx" | xargs grep -l -i "quantum" 2>/dev/null | wc -l)"
echo "   🐍 Scripts Python: $(find . -name "*.py" | xargs grep -l -i "quantum\|qiskit" 2>/dev/null | wc -l)"
echo "   📚 Documentação: $(find docs -name "*.md" | xargs grep -l -i "quantum" 2>/dev/null | wc -l)"

echo "✅ Busca otimizada concluída!"
