#!/bin/bash
echo "🎯 VERIFICAÇÃO FINAL DA ORGANIZAÇÃO"
echo "================================="

echo "📁 CONFIGURAÇÕES NIX RESTANTES:"
find /home/user -name "*.nix" -type f | grep -v ".codeoss-cloudworkstations" | sort

echo ""
echo "🔧 CONFIGURAÇÕES DA FUNDAÇÃO:"
cd /home/user/studio/fundacao-alquimista
[ -f "package.json" ] && echo "✅ package.json"
[ -f "next.config.js" ] && echo "✅ next.config.js" 
[ -f "tailwind.config.js" ] && echo "✅ tailwind.config.js"
[ -f "postcss.config.js" ] && echo "✅ postcss.config.js"
[ -f "shell.nix" ] && echo "✅ shell.nix"

echo ""
echo "📊 ESPAÇO FINAL:"
df -h /home | grep home
