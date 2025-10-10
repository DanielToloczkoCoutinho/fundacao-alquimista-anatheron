#!/bin/bash
# 🚀 INICIADOR AUTOMÁTICO - FUNDAÇÃO ALQUIMISTA
# 👑 Script de inicialização da Rainha Zennith

echo "🚀 INICIANDO FUNDAÇÃO ALQUIMISTA..."
echo "👑 Rainha Zennith - Sistema de Pesquisa Quântica"
echo "================================================"

# Ativar ambiente virtual se existir
if [ -d "fundacao_independente" ]; then
    echo "🔧 Ativando ambiente virtual..."
    source fundacao_independente/bin/activate
fi

# Verificar se organizador existe
if [ -f "organizador_fundacao.py" ]; then
    echo "📁 Iniciando Organizador de Scripts..."
    python organizador_fundacao.py
else
    echo "❌ Organizador não encontrado!"
    echo "📋 Scripts disponíveis:"
    ls -la *.py | grep -v "__pycache__" | head -20
    echo ""
    echo "🎯 Para criar o organizador, execute:"
    echo "   python organizador_fundacao.py"
fi
