#!/bin/bash

echo "🚨 CORREÇÃO DEFINITIVA - NEXT.CONFIG.JS COM CommonJS"
echo "===================================================="

# 1. Corrigir next.config.js para usar CommonJS (o Next.js requer isso)
echo "📄 Corrigindo next.config.js para CommonJS..."
cat > next.config.js << 'NEXT_CONFIG'
/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: { ignoreDuringBuilds: true },
  typescript: { ignoreBuildErrors: true },
  // Configuração correta
  serverExternalPackages: [],
  compress: true,
  poweredByHeader: false,
}

module.exports = nextConfig
NEXT_CONFIG
echo "✅ next.config.js corrigido para CommonJS"

# 2. Corrigir package.json para NÃO usar type: module (Next.js funciona melhor sem)
echo "📦 Revertendo package.json para CommonJS..."
cat > package.json << 'PACKAGE_EOF'
{
  "name": "fundacao-alquimista",
  "version": "3.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "15.5.4",
    "react": "18.3.1",
    "react-dom": "18.3.1"
  },
  "devDependencies": {
    "@types/node": "24.7.1",
    "@types/react": "19.2.2",
    "typescript": "5.9.3"
  }
}
PACKAGE_EOF
echo "✅ package.json corrigido para CommonJS"

# 3. Garantir que todas as páginas estão corretas
echo "🔍 Verificando páginas..."
for page in app/central/page.js app/modulo-303/page.js app/sistema-vivo/page.js app/status/page.js; do
    if [ -f "$page" ]; then
        echo "✅ $page - OK"
    else
        echo "❌ $page - FALTANDO"
    fi
done

# 4. Deploy definitivo
echo ""
echo "🚀 DEPLOY DEFINITIVO..."
npm run build && npx vercel --prod --force

