#!/bin/bash
# 🔄 SCRIPT DE SINCRONIZAÇÃO UNIFICADA

echo "🔄 INICIANDO SINCRONIZAÇÃO DO SISTEMA MULTIDIMENSIONAL..."

# 1. Sincronizar estrutura do organized_project
echo "📁 Sincronizando organized_project..."
cd /home/user/studio/fundacao-alquimista-luxnet/fundacao_unificada/organized_project
git add .
git commit -m "🔄 Sync automático - $(date +"%Y%m%d_%H%M%S")"
git push origin main

# 2. Atualizar portal Next.js com novos módulos
echo "🌐 Atualizando portal Next.js..."
cd /home/user/studio/fundacao-alquimista-quantica
npm run build

# 3. Sincronizar scripts centrais
echo "⚡ Sincronizando scripts centrais..."
cd /home/user/studio/SCRIPTS_CENTRALIZADOS
git add .
git commit -m "🔄 Sync scripts - $(date +"%Y%m%d_%H%M%S")"
git push origin main

# 4. Deploy automático
echo "🚀 Realizando deploy unificado..."
cd /home/user/studio/fundacao-alquimista-quantica
vercel --prod

echo "✅ SISTEMA UNIFICADO SINCRONIZADO!"
echo "🌐 Portal: https://fundacao-alquimista-4exompidd.vercel.app"
echo "🔬 Integration: https://fundacao-alquimista-4exompidd.vercel.app/integration"
