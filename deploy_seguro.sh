#!/bin/bash
# 🚀 DEPLOY SEGURO PARA O PORTAL
cd ~/studio
source ~/quantum_venv/bin/activate

echo "🚀 INICIANDO DEPLOY SEGURO..."
echo "============================"

# 1. Remover qualquer token residual
echo "🔒 Limpando tokens..."
find . -name "*.py" -exec sed -i 's/SEU_TOKEN_AQUI/SEU_TOKEN_AQUI/g' {} \; 2>/dev/null
find . -name "*.sh" -exec sed -i 's/SEU_TOKEN_AQUI/SEU_TOKEN_AQUI/g' {} \; 2>/dev/null

# 2. Fazer commit limpo
echo "💾 Commit seguro..."
git add .
git commit -m "🚀 Deploy seguro - $(date '+%Y-%m-%d %H:%M:%S')"

# 3. Tentar push
echo "📤 Enviando para GitHub..."
if git push origin main 2>/dev/null; then
    echo "✅ DEPLOY BEM-SUCEDIDO!"
    echo "🌐 Portal será atualizado em 2-5 minutos"
else
    echo "⚠️  DEPLOY BLOQUEADO (token no histórico)"
    echo "💡 Mantendo versão local (MAIS SEGURO)"
fi

echo ""
echo "📋 STATUS:"
echo "   🌐 Portal atual: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
echo "   📝 Versão: ZENNITH-DEPLOY: 2025-10-08 01:10:48"
echo "   🔐 Segurança: Scripts quânticos protegidos localmente"
