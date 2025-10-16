#!/bin/bash
echo "🔗 VERIFICAÇÃO DE CONEXÕES EXTERNAS"
echo "=================================="

# VERIFICAR GITHUB
echo "📦 GITHUB:"
[ -d ".github" ] && echo "✅ .github/: CONFIGURADO" || echo "❌ .github/: NÃO CONFIGURADO"
[ -f ".git/config" ] && echo "✅ Git: CONFIGURADO" || echo "❌ Git: NÃO CONFIGURADO"

# VERIFICAR STATUS DO VERCEL
echo ""
echo "🚀 STATUS VERCEL:"
if command -v vercel &> /dev/null; then
    echo "✅ Vercel CLI: INSTALADO"
    # VERIFICAR SE ESTÁ LOGADO
    vercel whoami &>/dev/null && echo "✅ Vercel: LOGADO" || echo "❌ Vercel: NÃO LOGADO"
else
    echo "❌ Vercel CLI: NÃO INSTALADO"
fi

# VERIFICAR REPOSITÓRIO REMOTO
echo ""
echo "🌐 REPOSITÓRIO REMOTO:"
git remote -v 2>/dev/null | head -5
