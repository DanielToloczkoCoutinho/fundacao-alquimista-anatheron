#!/bin/bash
echo "🔧 CORRIGINDO CONFIGURAÇÃO GIT DA FUNDAÇÃO"
echo "=========================================="

cd /home/user/studio

# 1. Limpar espaço
echo "🧹 Limpando espaço..."
rm -rf /home/user/backup_fundacao_20251009_215216 2>/dev/null
rm -rf node_modules/.cache 2>/dev/null
echo "✅ Espaço liberado"

# 2. Corrigir configuração
echo "🔧 Configurando Git..."
git remote set-url origin https://github.com/DanielToloczkoCoutinho/fundacao-alquimista.git
git config user.name "Daniel Toloczko Coutinho"
git config user.email "toloczkocoutinho@gmail.com"

# 3. Commit essencial
echo "🚀 Fazendo commit..."
git add app/ components/ public/ package.json next.config.js *.md
git commit -m "🏰 Fundação Alquimista - Sistema Completo Online

🌌 Status: 100% Operacional
🔬 Laboratórios: 6 especializados
🌐 URL: https://fundacao-alquimista-anatheron-fdzvusw18.vercel.app
👑 Autor: Daniel Toloczko Coutinho"

# 4. Push
echo "🌐 Enviando para GitHub..."
git push -u origin main

echo "🎉 CONFIGURAÇÃO CORRIGIDA!"
git log --oneline -2
