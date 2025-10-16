#!/bin/bash
echo "🎯 CHECKLIST DEFINITIVO - FUNDAÇÃO ALQUIMISTA"
echo "============================================"

echo "1. 🔗 GITHUB:"
git remote -v 2>/dev/null | grep -q "https" && echo "   ✅ HTTPS Configurado" || echo "   ❌ Problema com Git"
[ -d ".github" ] && echo "   ✅ .github/ presente" || echo "   ❌ .github/ ausente"

echo ""
echo "2. 🌐 VERCEL:"
[ -f "vercel.json" ] && echo "   ✅ vercel.json presente" || echo "   ❌ vercel.json ausente"
[ -d ".vercel" ] && echo "   ✅ .vercel/ presente" || echo "   ❌ .vercel/ ausente"
command -v vercel &>/dev/null && vercel whoami &>/dev/null && echo "   ✅ Logado no Vercel" || echo "   ❌ Não logado no Vercel"

echo ""
echo "3. 🔍 GOOGLE SEARCH CONSOLE:"
[ -f "app/layout.jsx" ] && grep -q "google-site-verification" app/layout.jsx && echo "   ✅ Meta tag presente" || echo "   ❌ Meta tag ausente"
[ -f "public/google865a57633873f213.html" ] && echo "   ✅ Arquivo verificação presente" || echo "   ❌ Arquivo verificação ausente"

echo ""
echo "4. 🏗️ BUILD:"
[ -f "package.json" ] && echo "   ✅ package.json presente" || echo "   ❌ package.json ausente"
[ -f "next.config.js" ] && echo "   ✅ next.config.js presente" || echo "   ❌ next.config.js ausente"

echo ""
echo "5. 📊 DEPENDÊNCIAS:"
npm list @prisma/client 2>/dev/null | grep -q "@prisma/client" && echo "   ✅ Prisma instalado" || echo "   ❌ Prisma ausente"
npm list three 2>/dev/null | grep -q "three" && echo "   ✅ Three.js instalado" || echo "   ❌ Three.js ausente"
npm list next-auth 2>/dev/null | grep -q "next-auth" && echo "   ✅ NextAuth instalado" || echo "   ❌ NextAuth ausente"

echo ""
echo "6. 🗂️ ESTRUTURA:"
[ -d "app" ] && echo "   ✅ app/ presente" || echo "   ❌ app/ ausente"
[ -d "public" ] && echo "   ✅ public/ presente" || echo "   ❌ public/ ausente"
[ -d "prisma" ] && echo "   ✅ prisma/ presente" || echo "   ❌ prisma/ ausente"
