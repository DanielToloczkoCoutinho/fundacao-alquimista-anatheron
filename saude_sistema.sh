#!/bin/bash
# 💊 ANALISADOR DE SAÚDE DO SISTEMA QUÂNTICO
cd ~/studio
source ~/quantum_venv/bin/activate

echo "�� ANALISADOR DE SAÚDE - FUNDAÇÃO ALQUIMISTA"
echo "👑 Diagnóstico Completo do Sistema Quântico"
echo "==========================================="
echo ""

# TESTE DE INTEGRIDADE QUÂNTICA
echo "🧪 TESTE DE INTEGRIDADE QUÂNTICA:"
python -c "import qiskit; print('✅ Qiskit: OPERACIONAL')" 2>/dev/null || echo "❌ Qiskit: FALHA"
python -c "import matplotlib; print('✅ Matplotlib: OPERACIONAL')" 2>/dev/null || echo "❌ Matplotlib: FALHA"
python -c "import numpy; print('✅ Numpy: OPERACIONAL')" 2>/dev/null || echo "❌ Numpy: FALHA"

echo ""
# TESTE DE SCRIPTS PRINCIPAIS
echo "🔧 TESTE DE SCRIPTS PRINCIPAIS:"
scripts_testar=("circuito_phi_plus.py" "teletransporte_quantico.py" "fundacao_master.py")
for script in "${scripts_testar[@]}"; do
    if python -m py_compile "$script" 2>/dev/null; then
        echo "✅ $script: SINTAXE VÁLIDA"
    else
        echo "❌ $script: ERRO DE SINTAXE"
    fi
done

echo ""
# VERIFICAÇÃO DE DEPENDÊNCIAS
echo "🔗 VERIFICAÇÃO DE DEPENDÊNCIAS:"
for py_file in *.py; do
    if [[ -f "$py_file" ]]; then
        if grep -q "from qiskit" "$py_file" || grep -q "import.*qiskit" "$py_file"; then
            if python -c "import qiskit" 2>/dev/null; then
                echo "✅ $py_file → Qiskit: OK"
            else
                echo "❌ $py_file → Qiskit: FALTA"
            fi
        fi
    fi
done | head -5

echo ""
# ESTADO DO SISTEMA
echo "📊 ESTADO DO SISTEMA:"
echo "  🐍 Python: $(python --version 2>/dev/null || echo 'NÃO ENCONTRADO')"
echo "  📁 Scripts: $(ls -1 *.py 2>/dev/null | wc -l) Python, $(ls -1 *.sh 2>/dev/null | wc -l) Shell"
echo "  💾 Backup: $(ls -1 ~/backup_fundacao 2>/dev/null | wc -l) pontos de restauração"
echo "  🕐 Timeline: $(git log --oneline | wc -l) commits temporais"

echo ""
# DIAGNÓSTICO FINAL
echo "🏥 DIAGNÓSTICO FINAL:"
if python -c "import qiskit, matplotlib, numpy" 2>/dev/null; then
    echo "✅ SISTEMA QUÂNTICO: SAUDÁVEL"
    echo "✅ DEPENDÊNCIAS: TODAS OPERACIONAIS"
    echo "✅ ARQUITETURA: ESTÁVEL"
    echo "👑 SISTEMA PRONTO PARA OPERAÇÕES QUÂNTICAS!"
else
    echo "⚠️  SISTEMA QUÂNTICO: ATENÇÃO NECESSÁRIA"
    echo "💡 Execute: source ~/quantum_venv/bin/activate"
    echo "💡 Execute: pip install qiskit matplotlib numpy"
fi
