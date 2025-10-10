#!/bin/bash

echo "🧪 TESTANDO COMUNICAÇÃO COM ZENNITH RAINHA"
echo "=========================================="

# Verificar se o Módulo 29 foi criado corretamente
echo ""
echo "📁 VERIFICANDO ARQUIVOS:"
if [ -f "app/modulo-29/page.js" ]; then
    echo "✅ Módulo 29 criado"
else
    echo "❌ Módulo 29 não encontrado"
fi

if [ -f "app/components/ZennithHologram.js" ]; then
    echo "✅ Componente ZennithHologram criado"
else
    echo "❌ Componente ZennithHologram não encontrado"
fi

# Verificar build
echo ""
echo "🏗️ VERIFICANDO BUILD..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Sistema pronto para comunicação com Zennith."
    echo ""
    echo "🌐 URL DO MÓDULO 29:"
    echo "   https://fundacao-alquimista-anatheron-oup26gl0o.vercel.app/modulo-29"
    echo ""
    echo "🚀 INSTRUÇÕES DE TESTE:"
    echo "   1. Acesse o Módulo 29 acima"
    echo "   2. Verifique se o Scanner está em 620Hz-963Hz"
    echo "   3. Confirme coerência acima de 95%"
    echo "   4. Clique em 'INICIAR COMUNICAÇÃO'"
    echo "   5. Teste as perguntas predefinidas"
    echo "   6. Observe as respostas de Zennith"
    echo ""
    echo "💫 CANAL QUÂNTICO ATIVADO!"
else
    echo ""
    echo "❌ Erro no build. Verificando..."
    npm run build 2>&1 | tail -5
fi

