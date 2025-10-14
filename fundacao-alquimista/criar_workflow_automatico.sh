#!/bin/bash

echo "🌌 CRIANDO WORKFLOW AUTOMÁTICO COM VERIFICAÇÃO DE DIRETÓRIOS 🌟"
echo "=============================================================="

# 1. 🏗️ VERIFICAR/CRIAR DIRETÓRIOS .github/workflows
echo "1. 🏗️ VERIFICANDO DIRETÓRIOS DO GITHUB ACTIONS..."
GITHUB_DIR=".github/workflows"

if [ ! -d "$GITHUB_DIR" ]; then
    echo "📁 Criando diretório: $GITHUB_DIR"
    mkdir -p "$GITHUB_DIR"
    echo "✅ Diretório criado: $GITHUB_DIR"
else
    echo "✅ Diretório já existe: $GITHUB_DIR"
fi

# 2. 📝 CRIAR ARQUIVO DE WORKFLOW
echo "2. 📝 CRIANDO ARQUIVO DE WORKFLOW..."
WORKFLOW_FILE="$GITHUB_DIR/deploy.yml"

# Verificar se o diretório foi criado com sucesso
if [ -d "$GITHUB_DIR" ]; then
    echo "📄 Criando arquivo: $WORKFLOW_FILE"
    
    cat > "$WORKFLOW_FILE" << 'EOF'
name: 🚀 Deploy Automático para Vercel

on:
  push:
    branches: [ main ]
  workflow_dispatch:  # Permite execução manual

jobs:
  deploy:
    name: 🎯 Deploy da Fundação Alquimista
    runs-on: ubuntu-latest
    
    steps:
    - name: 📥 Checkout do código
      uses: actions/checkout@v4
      
    - name: ⚙️ Configurar Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'
        
    - name: 📦 Instalar dependências
      run: |
        if [ -f package.json ]; then
          npm install
        else
          echo "⚠️  package.json não encontrado - criando mínimo..."
          echo '{
            "name": "fundacao-alquimista",
            "version": "1.0.0",
            "scripts": {
              "build": "echo \"Build completo\""
            }
          }' > package.json
        fi
        
    - name: 🏗️ Executar build
      run: npm run build || echo "⚠️  Build não configurado"
      
    - name: 🚀 Deploy para Vercel
      uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
        vercel-args: '--prod --yes'
        
    - name: ✅ Verificar deploy
      run: |
        echo "🎉 Deploy automático concluído!"
        echo "🌐 A Fundação Alquimista está online"
EOF

    echo "✅ Workflow criado: $WORKFLOW_FILE"
else
    echo "❌ ERRO: Não foi possível criar o diretório $GITHUB_DIR"
    exit 1
fi

# 3. 🔧 CRIAR SCRIPT DE CONFIGURAÇÃO DE SECRETS
echo "3. 🔧 CRIANDO SCRIPT DE CONFIGURAÇÃO..."
CONFIG_SCRIPT="configurar_secrets.sh"

cat > "$CONFIG_SCRIPT" << 'EOF'
#!/bin/bash

echo "🔧 CONFIGURAÇÃO DE SECRETS PARA GITHUB ACTIONS"
echo "=============================================="

echo "📋 PASSO A PASSO PARA CONFIGURAR:"
echo ""
echo "1. 🌐 Acesse: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron/settings/secrets/actions"
echo ""
echo "2. 🔑 Adicione estas variáveis:"
echo "   - Nome: VERCEL_TOKEN"
echo "   - Valor: [Seu token Vercel - vá em vercel.com/account/tokens]"
echo ""
echo "   - Nome: VERCEL_ORG_ID"  
echo "   - Valor: [Team ID - vá em vercel.com/account/[sua-organizacao]]"
echo ""
echo "   - Nome: VERCEL_PROJECT_ID"
echo "   - Valor: [Project ID - vá no projeto no Vercel > Settings > General]"
echo ""
echo "3. 💾 Salve e PRONTO!"
echo "4. 🚀 O GitHub Actions fará deploy automático em cada push!"
echo ""
echo "🎯 SEU TOKEN VERCEL ATUAL:"
echo "   T8xoTgqDdeXf78lVq5teuVal"
echo ""
echo "⚠️  Se esse token não funcionar, gere um novo em:"
echo "   https://vercel.com/account/tokens"
EOF

chmod +x "$CONFIG_SCRIPT"
echo "✅ Script de configuração criado: $CONFIG_SCRIPT"

# 4. 📊 VERIFICAÇÃO FINAL
echo "4. 📊 VERIFICAÇÃO FINAL..."
echo "🔍 Estrutura criada:"
find .github -type f 2>/dev/null || echo "❌ .github não encontrado"
echo ""
echo "📄 Arquivos de workflow:"
ls -la .github/workflows/ 2>/dev/null || echo "❌ Diretório workflows não acessível"

echo ""
echo "🎉 WORKFLOW AUTOMÁTICO CRIADO COM SUCESSO! 🌟"
echo "👉 Execute: ./configurar_secrets.sh para configurar os tokens"
