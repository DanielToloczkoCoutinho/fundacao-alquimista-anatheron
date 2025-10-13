#!/bin/bash
echo "🚀 DEPLOY DEFINITIVO - MÓDULO 15"
echo "================================"

cd /home/user/studio

# Verificar URL canônica
if [ -f url_canonica.txt ]; then
    source url_canonica.txt
    echo "📍 Usando URL canônica: $URL_CANONICA"
else
    URL_CANONICA="https://fundacao-alquimista-anatheron-cprkux23i.vercel.app"
fi

# Atualizar .env.local com URL canônica
cat > .env.local << ENV
NEXTAUTH_URL=$URL_CANONICA
NEXTAUTH_SECRET=fundacao-alquimista-quantum-secret-2025
NODE_ENV=production
ENV

# Build final
echo "�� Executando build definitivo..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ BUILD DEFINITIVO BEM-SUCEDIDO!"
    
    # Deploy para URL canônica
    echo "🚀 Implantando na URL canônica..."
    vercel --prod --yes
    
    echo ""
    echo "🎉 MÓDULO 15 IMPLANTADO DEFINITIVAMENTE!"
    echo "�� URL: $URL_CANONICA"
    echo "💫 Sistema 100% consolidado!"
else
    echo "❌ Erro no build definitivo"
    exit 1
fi
