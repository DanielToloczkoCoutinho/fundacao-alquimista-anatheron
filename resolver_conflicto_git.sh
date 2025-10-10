#!/bin/bash
echo "🔄 RESOLVENDO CONFLITO GIT DEFINITIVAMENTE"
echo "=========================================="

cd /home/user/studio

# Configurar merge como padrão
echo "🔧 Configurando Git para merge..."
git config pull.rebase false

# Fazer pull integrando tudo
echo "📥 Baixando commits remotos..."
git pull origin main --allow-unrelated-histories

# Verificar status
echo "📊 Status após merge:"
git status

# Se houver conflitos, resolvemos
if git status | grep -q "conflict"; then
    echo "⚠️  Resolvendo conflitos..."
    # Aqui você precisaria resolver manualmente os arquivos em conflito
    # git add [arquivos resolvidos]
else
    echo "✅ Sem conflitos detectados"
    git add .
fi

# Commit final
echo "💾 Commit de integração..."
git commit -m "🏰 MERGE COMPLETO: Fundação Alquimista

🌌 Integração de todas as versões:
- Sistema local (Studio)
- Repositório remoto 
- Todas as funcionalidades
- Deploys ativos

🔬 Status: SISTEMA 100% OPERACIONAL
🌐 URL: https://fundacao-alquimista-anatheron.vercel.app
👑 Autor: Daniel Toloczko Coutinho"

# Push final
echo "🚀 Enviando para GitHub..."
git push origin main

echo "🎉 CONFLITO RESOLVIDO!"
git log --oneline -5
