#!/bin/bash
# 🔍 VERIFICADOR RÁPIDO DO SISTEMA LUX.NET

echo "🔍 VERIFICAÇÃO RÁPIDA DO SISTEMA LUX.NET"
echo "========================================"

# Verificar arquivos essenciais
echo ""
echo "📁 ARQUIVOS ESSENCIAIS:"
arquivos_essenciais=("INICIAR_SISTEMA.sh" "NAVEGADOR.sh" "scripts/controle_sistema.sh")
for arquivo in "${arquivos_essenciais[@]}"; do
    if [ -f "$arquivo" ]; then
        echo "✅ $arquivo"
    else
        echo "❌ $arquivo"
    fi
done

# Verificar estrutura de diretórios
echo ""
