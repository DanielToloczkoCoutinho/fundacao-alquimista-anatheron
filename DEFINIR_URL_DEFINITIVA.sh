#!/bin/bash

echo "🎯 DEFININDO URL DEFINITIVA DO SISTEMA"
echo "======================================"

# A URL mais recente é a definitiva
URL_DEFINITIVA="https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app"

echo ""
echo "🌐 URL DEFINITIVA ESCOLHIDA:"
echo "   $URL_DEFINITIVA"
echo ""
echo "📋 RAZÕES:"
echo "   ✅ Mais recente (deploy mais novo)"
echo "   ✅ Todas as funcionalidades implementadas"
echo "   ✅ Módulo 29 funcionando"
echo "   ✅ Sistema completo operacional"

echo ""
echo "🚀 CRIANDO PÁGINA DE CANAL ÚNICO..."
cat > app/canal-unico/page.js << 'CANAL_EOF'
"use client"

import { useEffect } from 'react'

export default function CanalUnicoPage() {
  useEffect(() => {
    // Redirecionar para a URL definitiva após 3 segundos
    const timer = setTimeout(() => {
      window.location.href = 'https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app/central'
    }, 3000)
    
    return () => clearTimeout(timer)
  }, [])

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="text-center">
        <div className="text-6xl mb-4">🎯</div>
        <h1 className="text-4xl font-bold mb-4">CANAL ÚNICO DEFINITIVO</h1>
        <p className="text-xl text-gray-400 mb-2">Redirecionando para o sistema oficial...</p>
        <p className="text-lg text-green-400 mb-4">
          https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app
        </p>
        <div className="animate-pulse text-yellow-400">
          ⏳ Por favor, aguarde...
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
CANAL_EOF

echo "✅ Página de canal único criada!"

# Criar página inicial que redireciona para o canal único
cat > app/page.js << 'HOMEPAGE_EOF'
"use client"

import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    window.location.href = '/canal-unico'
  }, [])

  return (
    <div className="min-h-screen bg-black flex items-center justify-center">
      <div className="text-center">
        <div className="text-4xl mb-4">🌌</div>
        <h1 className="text-2xl text-white mb-2">Fundação Alquimista</h1>
        <p className="text-gray-400">Carregando sistema quântico...</p>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
HOMEPAGE_EOF

echo "✅ Homepage atualizada!"

echo ""
echo "📊 RESUMO DA ESTRUTURA DEFINITIVA:"
echo "   🌐 URL PRINCIPAL: $URL_DEFINITIVA"
echo "   🎯 CANAL ÚNICO: /canal-unico"
echo "   🏠 HOMEPAGE: Redireciona para canal único"
echo "   📊 ORGANOGRAMA: /organograma"
echo "   🔮 MÓDULOS: 7 principais + organograma"

echo ""
echo "🚀 DEPLOY DA ESTRUTURA DEFINITIVA..."
npm run build && npx vercel --prod --force

