#!/bin/bash
echo "🔬 ANÁLISE RÁPIDA DE TECNOLOGIAS"
echo "================================"

cd /home/user

# Tecnologias críticas para verificar rápido
tech_criticas=("qiskit" "tensorflow" "three" "webgl" "quantum")

for tech in "${tech_criticas[@]}"; do
    echo -n "🔍 $tech: "
    count=$(find . -name "*.py" -exec grep -l "$tech" {} \; 2>/dev/null | head -5 | wc -l)
    if [ $count -gt 0 ]; then
        echo "✅ $count sistemas"
        # Mostrar alguns exemplos
        find . -name "*.py" -exec grep -l "$tech" {} \; 2>/dev/null | head -2 | while read file; do
            echo "     📄 $(basename $file)"
        done
    else
        echo "❌ não encontrado"
    fi
done

echo ""
echo "�� TECNOLOGIAS IDENTIFICADAS:"
grep -r "import\\|from" /home/user/studio 2>/dev/null | grep -E "qiskit|tensorflow|three" | head -5
