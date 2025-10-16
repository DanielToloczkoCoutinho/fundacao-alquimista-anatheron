#!/bin/bash
echo "🔍 VERIFICAÇÃO DE METADADOS E INTEGRIDADE"
echo "========================================"

# VERIFICAR DEPENDÊNCIAS
echo "📦 VERIFICANDO DEPENDÊNCIAS:"
if [ -f "package.json" ]; then
    echo "   Node.js: $(node --version 2>/dev/null || echo 'Não instalado')"
    echo "   npm: $(npm --version 2>/dev/null || echo 'Não instalado')"
    echo "   Next.js: $(grep '"next"' package.json | head -1 | cut -d'"' -f4 || echo 'Não especificado')"
fi

# VERIFICAR ESTRUTURA NEXT.JS
echo ""
echo "🌐 VERIFICANDO ESTRUTURA NEXT.JS:"
[ -d "app" ] && echo "   ✅ App Router: configurado"
[ -d "pages" ] && echo "   ✅ Pages Router: configurado"
[ -f "next.config.js" ] && echo "   ✅ Next.js Config: presente"

# VERIFICAR ARQUIVOS DE VERIFICAÇÃO GOOGLE
echo ""
echo "🔍 VERIFICANDO CONFIGURAÇÕES GOOGLE:"
[ -f "public/google865a57633873f213.html" ] && echo "   ✅ Arquivo verificação Google: presente"
[ -f "app/layout.jsx" ] && grep -q "google-site-verification" app/layout.jsx && echo "   ✅ Meta tag Google: presente"

# VERIFICAR CONEXÕES EXTERNAS
echo ""
echo "🌐 CONEXÕES EXTERNAS:"
[ -d ".github" ] && echo "   ✅ GitHub: configurado"
[ -d ".vercel" ] && echo "   ✅ Vercel: configurado"
