#!/usr/bin/env nix-shell
#!nix-shell -i bash -p imagemagickBig nodejs git vercel

set -e

echo "🌌 INICIANDO O PROCESSO DE INTEGRAÇÃO E DEPLOY MULTIDIMENSIONAL..."

echo "📂 Criando módulo de integração se não existir..."
mkdir -p ~/studio/fundacao-alquimista-quantica/src/lib/integration

echo "💻 Rodando build Next.js no portal principal..."
cd ~/studio/fundacao-alquimista-quantica
npm install
npm run build

echo "🔄 Sincronizando Organized Project via git..."
cd ~/studio/fundacao-alquimista-luxnet/fundacao_unificada/organized_project
git add .
echo "Fazendo pull para evitar conflitos no push..."
git pull origin main --rebase || echo "Conflitos resolvidos manualmente ou nenhum conflito"
git commit -m "🔄 Sync automático - $(date +%Y%m%d_%H%M%S)" || echo "Nada para commitar"
git push origin main

echo "⚡ Sincronizando Scripts Centrais..."
cd ~/studio/SCRIPTS_CENTRALIZADOS
git add .
git pull origin main --rebase || echo "Conflitos resolvidos manualmente ou nenhum conflito"
git commit -m "🔄 Sync scripts - $(date +%Y%m%d_%H%M%S)" || echo "Nada para commitar"
git push origin main

# Verifica se CLI do Vercel está instalado
if ! command -v vercel &> /dev/null; then
  echo "CLI do Vercel não encontrado. Instalando globalmente..."
  npm install -g vercel
fi

echo "🚀 Executando deploy automático no Vercel..."
cd ~/studio/fundacao-alquimista-quantica
vercel --prod

echo "🔮 TESTE RÁPIDO DO PORTAL:"
echo "1. Acesse: https://fundacao-alquimista-diy297mf9.vercel.app/auth/signin"
echo "2. Login: ANATHERON"
echo "3. Senha: alchemista_2024"
echo "4. Verifique se vai para dashboard com nível quântico 11D"

echo "✅ Processo concluído! Acesse o portal em https://fundacao-alquimista-diy297mf9.vercel.app"

