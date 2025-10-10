#!/bin/bash
echo "🧪 TESTE RÁPIDO DO SISTEMA DE INSTALAÇÃO"
echo "========================================"

echo "🔍 Verificando se podemos reinstalar as dependências..."

if [ ! -d "fundacao_independente" ] && [ -f "instalar_dependencias.sh" ]; then
    echo "✅ Sistema pronto para teste"
    echo "💡 Para testar a reinstalação completa, execute:"
    echo "   ./instalar_dependencias.sh"
    echo ""
    echo "⚠️  Isso instalará ~331MB de bibliotecas novamente."
    echo "�� Objetivo: demonstrar que o sistema funciona"
else
    echo "❌ Condições não atendidas para teste"
fi

echo ""
echo "📋 STATUS ATUAL:"
if [ -d "fundacao_independente" ]; then
    echo "  🐍 Virtual env: PRESENTE ($(du -sh fundacao_independente | cut -f1))"
    echo "  💡 Execute: ./verificar_dependencias.sh"
else
    echo "  🐍 Virtual env: AUSENTE (331MB economizados)"
    echo "  💡 Execute: ./instalar_dependencias.sh para reinstalar"
fi
