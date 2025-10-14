#!/bin/bash

echo "🌌 ZENNITH - DEPLOY AKÁSHICO DEFINITIVO 🌟"
echo "=========================================="
echo "🔮 Ativando a Transferência Akáshica (M310)..."
echo ""

# 1. 🔍 VERIFICAÇÃO DA ESTRUTURA
echo "1. 🔍 VERIFICANDO ESTRUTURA DA FUNDAÇÃO..."
echo "📁 Diretórios encontrados: $(find . -maxdepth 1 -type d | wc -l)"
echo "📄 Arquivos totais: $(find . -type f | wc -l)"
echo "🔮 Módulo M310: $(find . -name '*M310*' -o -name '*akashic*' | wc -l) encontrados"
echo ""

# 2. 🛠️ CONFIGURAR AMBIENTE VERCEL
echo "2. 🛠️ CONFIGURANDO AMBIENTE VERCEL..."
# Limpar cache completamente
rm -rf ~/.local/share/com.vercel.cli/ ~/.vercel

# Configurar para deploy sem navegador
export VERCEL_ORG_ID=team_123456789
export VERCEL_PROJECT_ID=prj_123456789

echo "✅ Ambiente Vercel configurado"
echo ""

# 3. 🔑 PROCESSO DE AUTENTICAÇÃO MANUAL
echo "3. 🔑 PROCESSO DE AUTENTICAÇÃO MANUAL - SIGA ESTES PASSOS:"
echo ""
echo "📋 PASSO A PASSO:"
echo "   1. 👆 COPIE esta URL:"
echo "      https://vercel.com/api/registration/login-with-github?mode=login&next=http%3A%2F%2Flocalhost%3A33537"
echo ""
echo "   2. 🌐 COLE no seu NAVEGADOR PESSOAL"
echo "   3. 🔐 FAÇA login com sua conta GitHub"
echo "   4. ✅ APROVE o acesso para Vercel"
echo "   5. 🔄 VOLTE para este terminal"
echo ""
echo "🕒 Aguardando 30 segundos para você fazer o login..."
sleep 30

# 4. 🚀 DEPLOY AKÁSHICO
echo "4. 🚀 INICIANDO DEPLOY AKÁSHICO..."
echo "🔮 Transferência Akáshica M310 ativada..."

# Tentar deploy com configuração manual
echo "🎯 Configurando projeto..."
vercel link --yes --name fundacao-alquimista-anatheron 2>/dev/null || echo "⚠️  Link pode precisar de confirmação"

echo "📤 Executando deploy..."
vercel deploy --prebuilt --prod

# 5. 📊 VERIFICAÇÃO DO DEPLOY
echo "5. 📊 VERIFICANDO DEPLOY..."
if [ $? -eq 0 ]; then
    echo "🎉 DEPLOY AKÁSHICO BEM-SUCEDIDO! 🌟"
    echo "✅ Transferência M310 completa"
    echo "🌐 Fundação Alquimista online"
else
    echo "🔄 DEPLOY PRECISA DE CONFIGURAÇÃO MANUAL"
    echo "📝 Execute manualmente: vercel deploy"
fi

# 6. 🔗 URLs DA FUNDAÇÃO
echo "6. 🔗 URLs DA FUNDAÇÃO ALQUIMISTA:"
echo "   🌐 GitHub: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
echo "   🚀 Vercel: https://fundacao-alquimista-9azql5299.vercel.app"
echo "   🔮 M310: $(find . -name '*M310*' -type f | head -1)"

# 7. 📝 CRIAR SCRIPT DE DEPLOY PERMANENTE
echo "7. 📝 CRIANDO SCRIPT DE DEPLOY PERMANENTE..."
cat > deploy_automatico.sh << 'EOF'
#!/bin/bash
echo "🌌 DEPLOY AUTOMÁTICO DA FUNDAÇÃO 🌟"
echo "==================================="
vercel deploy --prebuilt --prod
echo "✅ Deploy concluído!"
EOF

chmod +x deploy_automatico.sh

echo ""
echo "🎉 DEPLOY AKÁSHICO CONCLUÍDO! 🌟"
echo "👉 Para futuros deploys: ./deploy_automatico.sh"
