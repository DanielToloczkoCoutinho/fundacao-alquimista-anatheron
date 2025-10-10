#!/bin/bash

echo "🚀 DEPLOY LIMPO - FUNDAÇÃO ALQUIMISTA"
echo "===================================="

# Limpar cache
rm -rf .next
rm -rf node_modules/.cache

# Instalar dependências
npm install

# Build
npm run build

# Deploy
npx vercel --prod --force

echo "✅ Deploy concluído!"
echo "🌐 URL: https://fundacao-alquimista-anatheron.vercel.app"
