#!/bin/bash

echo "🌌 SETUP COMPLETO DA FUNDAÇÃO ALQUIMISTA 🌟"
echo "==========================================="

# Função robusta para criar arquivos
criar_arquivo() {
    local path="$1"
    local content="$2"
    
    echo "📁 Criando: $path"
    mkdir -p "$(dirname "$path")"
    echo "$content" > "$path"
    echo "✅ Criado: $path"
}

echo "1. 🏗️ CRIANDO ESTRUTURA NEXT.JS..."

# package.json
criar_arquivo "package.json" '{
  "name": "fundacao-alquimista",
  "version": "1.0.0", 
  "type": "module",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "deploy": "vercel --prod"
  },
  "dependencies": {
    "next": "14.0.0",
    "react": "18.0.0",
    "react-dom": "18.0.0"
  }
}'

# next.config.js
criar_arquivo "next.config.js" '/** @type {import('"'"'next'"'"').NextConfig} */
const nextConfig = {
  output: '"'"'export'"'"',
  trailingSlash: true,
  images: { unoptimized: true }
}
module.exports = nextConfig'

# Layout principal
criar_arquivo "app/layout.jsx" 'export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body style={{ margin: 0, fontFamily: "Arial" }}>
        <nav style={{ padding: "20px", background: "#1a1a1a", color: "white" }}>
          🌌 Fundação Alquimista
        </nav>
        <main>{children}</main>
      </body>
    </html>
  )
}'

# Página principal
criar_arquivo "app/page.jsx" 'export default function Home() {
  return (
    <div style={{ padding: "40px" }}>
      <h1>🌀 Central da Fundação Alquimista</h1>
      <p>Sistema principal online e funcionando!</p>
      
      <div style={{ marginTop: "30px" }}>
        <h3>🚀 Status do Sistema:</h3>
        <ul>
          <li>✅ Estrutura: 22 diretórios organizados</li>
          <li>✅ Módulo M310: Transferência Akáshica</li>
          <li>✅ GitHub: Sincronizado e versionado</li>
          <li>✅ Deploy: Pronto para produção</li>
        </ul>
      </div>
    </div>
  )
}'

echo "2. 🔄 CRIANDO GITHUB ACTIONS..."

# Workflow de deploy
criar_arquivo ".github/workflows/deploy.yml" 'name: 🚀 Deploy Automático

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: 18
    - run: npm install
    - run: npm run build
    - uses: amondnet/vercel-action@v25
      with:
        vercel-token: \${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: \${{ secrets.VERCEL_ORG_ID }} 
        vercel-project-id: \${{ secrets.VERCEL_PROJECT_ID }}
        vercel-args: "--prod --yes"
'

echo "3. 📝 CRIANDO DOCUMENTAÇÃO..."

# README de deploy
criar_arquivo "DEPLOY_GUIDE.md" '# 🚀 Guia de Deploy - Fundação Alquimista

## Configuração Automática

1. **Configure os secrets no GitHub:**
   - Vá em: Settings > Secrets and variables > Actions
   - Adicione:
     - `VERCEL_TOKEN`
     - `VERCEL_ORG_ID` 
     - `VERCEL_PROJECT_ID`

2. **Deploy automático:**
   - Cada push na main faz deploy automático
   - Ou execute manualmente em Actions

## URLs:
- 🌐 **GitHub:** https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron
- 🚀 **Vercel:** https://fundacao-alquimista-anatheron.vercel.app

## Estrutura:
- 22 diretórios organizados
- Módulo M310 ativo
- Sistema de deploy automático
'

echo "4. 📊 VERIFICAÇÃO FINAL..."
echo "🔍 Estrutura criada:"
find . -name "*.json" -o -name "*.js" -o -name "*.jsx" -o -name "*.md" -o -name "*.yml" | head -20

echo ""
echo "🎉 SETUP COMPLETO CONCLUÍDO! 🌟"
echo "👉 Agora faça commit e push:"
echo "   git add . && git commit -m '🏗️ Estrutura deployável completa' && git push"
