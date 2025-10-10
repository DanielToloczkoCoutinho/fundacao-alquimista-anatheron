#!/bin/bash
# 🌐 ATUALIZADOR DO PORTAL DA FUNDAÇÃO
cd ~/studio
source ~/quantum_venv/bin/activate

echo "🌐 VERIFICANDO ATUALIZAÇÃO DO PORTAL..."
echo "====================================="

# Verificar se tem conexão com GitHub
if git remote -v | grep -q "github.com"; then
    echo "✅ GitHub conectado"
    
    # Verificar diferenças entre local e remoto
    LOCAL_COMMITS=$(git log --oneline | wc -l)
    REMOTE_COMMITS=$(git log origin/main --oneline 2>/dev/null | wc -l)
    
    echo "📊 Commits locais: $LOCAL_COMMITS"
    echo "📊 Commits remotos: $REMOTE_COMMITS"
    
    if [ "$LOCAL_COMMITS" -gt "$REMOTE_COMMITS" ]; then
        echo "🔄 Commits locais não sincronizados"
        echo "⚠️  Portal NÃO será atualizado automaticamente"
        echo "💡 Motivo: Token bloqueou push anteriormente"
    else
        echo "✅ Portal sincronizado"
    fi
else
    echo "❌ GitHub não conectado"
fi

echo ""
echo "🎯 SITUAÇÃO ATUAL:"
echo "   O portal está funcionando na versão:"
echo "   ZENNITH-DEPLOY: 2025-10-08 01:10:48"
echo ""
echo "🔧 SOLUÇÃO:"
echo "   Os novos scripts ficam LOCAIS (mais seguro)"
echo "   O portal público continua ESTÁVEL"
echo ""
echo "🌐 PORTAL: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
echo "👤 qualquer usuário | 🔑 alchemista_2024"

# Testar se o portal está online
echo ""
echo "🔍 TESTANDO PORTAL..."
curl -s -I https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/ | head -1
