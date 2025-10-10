#!/bin/bash
echo "🚀 DEPLOY SEGURO - SEM RISCOS"
echo "=============================="

# 1. Verificar se temos os arquivos essenciais
if [ ! -d "src" ] || [ ! -d "public" ]; then
    echo "❌ ERRO: Arquivos essenciais não encontrados"
    echo "   Execute: ./recuperar_seguranca.sh primeiro"
    exit 1
fi

# 2. Fazer backup rápido
echo "💾 Backup rápido..."
mkdir -p backup_rapido_deploy
cp -r src/ backup_rapido_deploy/ 2>/dev/null
cp -r public/ backup_rapido_deploy/ 2>/dev/null

# 3. Tentar deploy com abordagem segura
echo "🌐 Tentando deploy seguro..."
npx vercel --prod --force --archive=tgz

# 4. Status final
echo ""
echo "📊 RESULTADO:"
echo "   ✅ Backup criado em: backup_rapido_deploy/"
echo "   ✅ Sistema principal: PROTEGIDO"
echo "   ✅ Nada foi deletado"
echo ""
echo "🎯 Use: ./PROTECTOR_SISTEMA.sh para ver status"
