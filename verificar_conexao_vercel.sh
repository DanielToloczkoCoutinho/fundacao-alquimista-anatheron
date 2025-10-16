#!/bin/bash
echo "🚀 VERIFICANDO CONEXÃO COM VERCEL"
echo "================================"

# VERIFICAR LOGIN VERCEL
echo "🔐 STATUS LOGIN:"
vercel whoami 2>/dev/null && echo "✅ LOGADO NO VERCEL" || echo "❌ NÃO LOGADO - PRECISA: vercel login"

# VERIFICAR PROJETOS VERCEL
echo ""
echo "📦 PROJETOS VERCEL:"
vercel list 2>/dev/null | head -10 || echo "❌ Não consegui listar projetos"

# VERIFICAR DEPLOYMENTS
echo ""
echo "🌐 DEPLOYMENTS ATIVOS:"
vercel ls 2>/dev/null | grep "fundacao-alquimista" | head -10 || echo "❌ Não consegui listar deployments"
