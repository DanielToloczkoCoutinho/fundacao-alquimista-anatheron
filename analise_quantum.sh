#!/bin/bash
echo "🔮 ANÁLISE DO AMBIENTE QUANTUM"
echo "=============================="

# VERIFICAR QUANTUM_VENV
echo "🐍 QUANTUM_VENV (504MB):"
if [ -d "/home/user/quantum_venv" ]; then
    echo "   ✅ PRESENTE: $(du -sh /home/user/quantum_venv | cut -f1)"
    echo "   📁 Estrutura:"
    ls -la /home/user/quantum_venv/ | head -10
else
    echo "   ❌ AUSENTE"
fi

# VERIFICAR MÓDULOS QUÂNTICOS
echo ""
echo "📚 MÓDULOS QUÂNTICOS:"
find . -name "*quantum*" -type f | head -10
find . -name "*qiskit*" -type f | head -5

# VERIFICAR CIRCUITOS QUÂNTICOS
echo ""
echo "⚡ CIRCUITOS QUÂNTICOS:"
find . -name "*circuito*" -type f | head -10
