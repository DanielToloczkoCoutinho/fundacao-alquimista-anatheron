#!/bin/bash
echo "🔍 INVESTIGANDO REPOSITÓRIO REMOTO"
echo "================================"

# VERIFICAR SE TEMOS ACESSO AO REMOTO
echo "🌐 REPOSITÓRIO REMOTO:"
git remote -v

# TENTAR BAIXAR INFORMAÇÕES DO REMOTO
echo ""
echo "📥 VERIFICANDO CONFIGURAÇÕES REMOTAS:"
git fetch --all 2>/dev/null && echo "✅ Conectado ao remoto" || echo "❌ Problema com remoto"

# VERIFICAR SE HÁ CONFIGURAÇÕES NO REMOTO
echo ""
echo "🔧 CONFIGURAÇÕES NO REMOTO:"
git show origin/main:vercel.json 2>/dev/null && echo "✅ vercel.json NO REMOTO" || echo "❌ vercel.json AUSENTE NO REMOTO"
git show origin/main:app/layout.jsx 2>/dev/null && echo "✅ app/layout.jsx NO REMOTO" || echo "❌ app/layout.jsx AUSENTE NO REMOTO"

# VERIFICAR COMMIT DO DEPLOY ATUAL
echo ""
echo "🚀 DEPLOY ATUAL NO VERCEL:"
echo "Commit: 8c2028d (SISTEMA 100% CORRIGIDO)"
git log --oneline -10 2>/dev/null | head -5
