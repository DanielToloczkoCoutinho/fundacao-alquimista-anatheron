#!/bin/bash
# 🌌 ATIVAÇÃO DEFINITIVA DA FUNDAÇÃO ALQUIMISTA
# 👑 Ativa virtualenv e executa tudo corretamente

echo "🔮 ATIVANDO AMBIENTE QUÂNTICO..."
source ~/quantum_venv/bin/activate

echo "🎯 VERIFICANDO INSTALAÇÕES..."
python -c "import qiskit; print('✅ Qiskit instalado')" || pip install qiskit
python -c "import matplotlib; print('✅ Matplotlib instalado')" || pip install matplotlib

echo "🧪 EXECUTANDO EXPERIMENTOS QUÂNTICOS..."
python fundacao_master.py

echo "🌐 ABRINDO PORTAL..."
python -c "import webbrowser; webbrowser.open('https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/')"

echo "📋 CREDENCIAIS:"
echo "   👤 Usuário: qualquer usuário"
echo "   🔑 Senha: alchemista_2024"
echo "🎉 FUNDAÇÃO ATIVADA!"
