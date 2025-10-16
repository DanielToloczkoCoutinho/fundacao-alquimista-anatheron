#!/bin/bash
echo "⚙️ VERIFICAÇÃO DE PRÉ-REQUISITOS"
echo "=============================="

# VERIFICAR NODE.JS E NPM
echo "🔧 AMBIENTE NODE.JS:"
echo "   Node.js: $(node --version 2>/dev/null || echo 'NÃO INSTALADO')"
echo "   npm: $(npm --version 2>/dev/null || echo 'NÃO INSTALADO')"
echo "   Next.js: $(grep '"next"' package.json | cut -d'"' -f4 2>/dev/null || echo 'NÃO ESPECIFICADO')"

# VERIFICAR ESTRUTURA NEXT.JS
echo ""
echo "🏗️ ESTRUTURA NEXT.JS:"
[ -d "app" ] && echo "   ✅ App Router: CONFIGURADO" || echo "   ❌ App Router: NÃO CONFIGURADO"
[ -f "next.config.js" ] && echo "   ✅ Next Config: PRESENTE" || echo "   ❌ Next Config: AUSENTE"

# VERIFICAR MEMÓRIA DISPONÍVEL
echo ""
echo "💾 RECURSOS DO SISTEMA:"
echo "   Memória RAM: $(free -h | grep Mem | awk '{print $4}') disponível"
echo "   Espaço disco: $(df -h /home | grep home | awk '{print $4}') disponível"
