#!/bin/bash
echo "🔍 VERIFICANDO ESTRUTURA DO PROJETO:"

# Verificar estrutura básica
echo "📁 Estrutura de pastas:"
find . -type d -name "app" -o -name "pages" | head -10

echo ""
echo "📄 Arquivos Next.js críticos:"
ls -la next.config.* 2>/dev/null || echo "❌ Next config não encontrado"
ls -la package.json 2>/dev/null || echo "❌ Package.json não encontrado"
ls -la src/app/ 2>/dev/null || echo "❌ src/app não encontrado"

echo ""
echo "🔧 Scripts no package.json:"
node -e "console.log(JSON.parse(require('fs').readFileSync('package.json')).scripts)" 2>/dev/null || echo "❌ Não foi possível ler scripts"

echo ""
echo "🌐 Rotas disponíveis:"
find src/app -name "page.tsx" 2>/dev/null | while read file; do
  route=$(echo $file | sed 's|src/app||' | sed 's|/page.tsx||' | sed 's|/index||')
  if [ -z "$route" ]; then route="/"; fi
  echo "✅ $route"
done
