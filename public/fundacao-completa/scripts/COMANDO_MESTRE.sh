#!/bin/bash

echo "🌌 SISTEMA ALQUIMISTA CÓSMICO - CONTROLE CENTRAL"
echo "================================================"
echo "💫 Iniciando todos os sistemas..."
echo ""

# 1. VERIFICAR SEGURANÇA
echo "🛡️ VERIFICANDO SEGURANÇA..."
./VERIFICACAO_SEGURANCA.sh

# 2. BACKUP AUTOMÁTICO
echo "🔮 EXECUTANDO BACKUP..."
./SISTEMA_BACKUP_AUTOMATICO.sh

# 3. MONITORAMENTO
echo "📊 INICIANDO MONITORAMENTO..."
./MONITORAMENTO_AVANCADO.sh

# 4. LABORATÓRIOS
echo "🔬 ATIVANDO LABORATÓRIOS..."
./ATIVAR_LABORATORIOS.sh

# 5. EXPANSÃO DIMENSIONAL
echo "🌀 EXPANDINDO DIMENSÕES..."
./EXPANSAO_DIMENSIONAL.sh

# 6. PERFORMANCE
echo "⚡ OTIMIZANDO PERFORMANCE..."
./OTIMIZAR_PERFORMANCE.sh

echo ""
echo "🎉 SISTEMA ALQUIMISTA CÓSMICO - OPERAÇÃO COMPLETA!"
echo "🚀 Pronto para expansão galáctica!"

# Mostrar status final
echo ""
echo "📊 STATUS FINAL:"
find . -name "status_sistema.json" -o -name "*.md" | head -5 | while read file; do
    echo "📄 $file"
done
