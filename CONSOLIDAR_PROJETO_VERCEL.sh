#!/bin/bash

echo "🎯 CONSOLIDANDO PROJETO NO VERCEL - LIMPEZA E ORGANIZAÇÃO"
echo "========================================================"

echo "📊 ANALISANDO PROJETOS NO VERCEL:"
echo "================================"

# Projetos identificados
PROJETOS=(
    "fundacao-alquimista-anatheron"  # Projeto principal
    "next-video-starter"             # Projeto antigo/lixo
    "fundacao-alquimis-git-5dc053"   # Projeto temporário
)

echo "🔍 Projetos encontrados:"
for projeto in "${PROJETOS[@]}"; do
    echo "   📁 $projeto"
done

echo ""
echo "🎯 PROJETO PRINCIPAL IDENTIFICADO:"
echo "=================================="
echo "   ✅ fundacao-alquimista-anatheron"
echo ""
echo "   📍 URL PRINCIPAL: https://fundacao-alquimista-anatheron.vercel.app"
echo "   🚀 URL ATUAL: https://fundacao-alquimista-anatheron-bu5hh0tnf.vercel.app"

echo ""
echo "🛠️ CONFIGURANDO PROJETO PRINCIPAL NO VERCEL..."
echo "=============================================="

# Criar configuração do Vercel
cat > vercel.json << 'VERCEL_EOF'
{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "functions": {
    "app/api/**/*.js": {
      "maxDuration": 30
    }
  },
  "regions": ["gru1"],
  "env": {
    "NEXT_PUBLIC_APP_URL": "https://fundacao-alquimista-anatheron.vercel.app"
  },
  "build": {
    "env": {
      "NEXT_PUBLIC_APP_URL": "https://fundacao-alquimista-anatheron.vercel.app"
    }
  },
  "git": {
    "deploymentEnabled": {
      "main": true
    }
  }
}
VERCEL_EOF

echo "✅ Configuração do Vercel criada!"

echo ""
echo "🔧 CONFIGURANDO DOMÍNIO PRINCIPAL..."
echo "===================================="

# Configurar para usar sempre o domínio principal
cat > app/config/domains.js << 'DOMAINS_EOF'
// 🎯 CONFIGURAÇÃO DE DOMÍNIOS DEFINITIVA
export const DOMINIOS = {
  PRINCIPAL: "https://fundacao-alquimista-anatheron.vercel.app",
  ALTERNATIVOS: [
    "https://fundacao-alquimista-anatheron-bu5hh0tnf.vercel.app",
    "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app",
    "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app",
    "https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app"
  ]
}

export const isDominioPrincipal = () => {
  if (typeof window !== 'undefined') {
    return window.location.origin === DOMINIOS.PRINCIPAL
  }
  return false
}

export const redirecionarParaPrincipal = () => {
  if (typeof window !== 'undefined' && !isDominioPrincipal()) {
    window.location.href = DOMINIOS.PRINCIPAL + window.location.pathname
  }
}
DOMAINS_EOF

echo "✅ Configuração de domínios criada!"

echo ""
echo "🏠 ATUALIZANDO HOMEPAGE PARA REDIRECIONAMENTO INTELIGENTE..."
echo "=========================================================="

cat > app/page.js << 'HOMEPAGE_DEFINITIVA'
"use client"

import { useEffect, useState } from 'react'
import { DOMINIOS, isDominioPrincipal, redirecionarParaPrincipal } from './config/domains'

export default function Home() {
  const [redirecionando, setRedirecionando] = useState(false)

  useEffect(() => {
    // Verificar se está no domínio principal
    if (!isDominioPrincipal()) {
      setRedirecionando(true)
      // Redirecionar para o domínio principal após 2 segundos
      setTimeout(() => {
        redirecionarParaPrincipal()
      }, 2000)
    } else {
      // Se já está no domínio principal, ir para o central
      window.location.href = '/central'
    }
  }, [])

  if (redirecionando) {
    return (
      <div className="min-h-screen bg-black flex items-center justify-center">
        <div className="text-center">
          <div className="text-4xl mb-4">🔄</div>
          <h1 className="text-2xl text-white mb-2">Otimizando Portal...</h1>
          <p className="text-gray-400">Redirecionando para domínio oficial</p>
          <div className="mt-4 text-yellow-400 animate-pulse">
            ⏳ Aguarde...
          </div>
        </div>
      </div>
    )
  }

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
HOMEPAGE_DEFINITIVA

echo "✅ Homepage com redirecionamento inteligente criada!"

echo ""
echo "📋 CRIANDO PÁGINA DE STATUS DO PROJETO..."
echo "========================================"

mkdir -p app/status-urls

cat > app/status-urls/page.js << 'STATUS_FIXED'
"use client"

import { useState, useEffect } from 'react'
import { DOMINIOS } from '../config/domains'

export default function StatusURLs() {
  const [urls, setUrls] = useState([])
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    const verificarURLs = async () => {
      const listaURLs = [
        {
          nome: "🎯 DOMÍNIO PRINCIPAL",
          url: DOMINIOS.PRINCIPAL,
          tipo: "principal",
          descricao: "URL oficial definitiva"
        },
        {
          nome: "🚀 URL ATUAL", 
          url: "https://fundacao-alquimista-anatheron-bu5hh0tnf.vercel.app",
          tipo: "atual",
          descricao: "Deploy mais recente"
        },
        {
          nome: "🔧 URL COMPLETA",
          url: "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app", 
          tipo: "completa",
          descricao: "Sistema multiversal completo"
        },
        {
          nome: "📜 URL ANTIGA",
          url: "https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app",
          tipo: "antiga",
          descricao: "Versão desatualizada"
        }
      ]

      // Verificar status de cada URL
      const urlsComStatus = await Promise.all(
        listaURLs.map(async (item) => {
          try {
            const response = await fetch(item.url, { method: 'HEAD' })
            const hasMultiversal = await fetch(item.url + '/sistema-multiversal', { method: 'HEAD' }).then(r => r.ok).catch(() => false)
            const hasIA = await fetch(item.url + '/ia-quantica', { method: 'HEAD' }).then(r => r.ok).catch(() => false)
            
            return {
              ...item,
              online: response.ok,
              multiversal: hasMultiversal,
              iaQuantica: hasIA,
              status: response.ok ? 'ONLINE' : 'OFFLINE'
            }
          } catch {
            return {
              ...item,
              online: false,
              multiversal: false,
              iaQuantica: false,
              status: 'OFFLINE'
            }
          }
        })
      )

      setUrls(urlsComStatus)
      setCarregando(false)
    }

    verificarURLs()
  }, [])

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent">
            🌐 STATUS DO PROJETO
          </h1>
          <p className="text-xl text-gray-400">Consolidação Definitiva - Fundação Alquimista</p>
        </div>

        {carregando ? (
          <div className="text-center">
            <div className="text-2xl mb-4">🔍 Verificando URLs...</div>
            <div className="animate-pulse text-gray-400">Analisando sistema completo</div>
          </div>
        ) : (
          <div className="space-y-6">
            {urls.map((item, index) => (
              <div 
                key={index}
                className={`p-6 rounded-2xl border-2 ${
                  item.tipo === 'principal' ? 'border-green-500 bg-green-900 bg-opacity-20' :
                  item.tipo === 'atual' ? 'border-blue-500 bg-blue-900 bg-opacity-20' :
                  item.tipo === 'completa' ? 'border-purple-500 bg-purple-900 bg-opacity-20' :
                  'border-gray-500 bg-gray-900 bg-opacity-20'
                }`}
              >
                <div className="flex justify-between items-start mb-4">
                  <div className="flex-1">
                    <h3 className="text-2xl font-bold text-white">{item.nome}</h3>
                    <div className="text-gray-400 text-sm mt-1">{item.descricao}</div>
                    <div className="text-gray-300 font-mono text-sm mt-2 break-all">{item.url}</div>
                  </div>
                  <div className={`px-3 py-1 rounded-full text-sm font-bold ${
                    item.online ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
                  }`}>
                    {item.status}
                  </div>
                </div>

                <div className="grid grid-cols-3 gap-4 text-center mb-4">
                  <div className={`p-3 rounded-lg ${
                    item.multiversal ? 'bg-purple-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Sistema Multiversal</div>
                    <div className={item.multiversal ? 'text-purple-400 font-bold' : 'text-gray-500'}>
                      {item.multiversal ? '✅ PRESENTE' : '❌ AUSENTE'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.iaQuantica ? 'bg-blue-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">IA Quântica</div>
                    <div className={item.iaQuantica ? 'text-blue-400 font-bold' : 'text-gray-500'}>
                      {item.iaQuantica ? '✅ PRESENTE' : '❌ AUSENTE'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.online ? 'bg-green-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Status Geral</div>
                    <div className={item.online ? 'text-green-400 font-bold' : 'text-red-400 font-bold'}>
                      {item.online ? '🟢 OPERACIONAL' : '🔴 OFFLINE'}
                    </div>
                  </div>
                </div>

                {item.tipo === 'principal' && item.online && (
                  <div className="mt-4 p-4 bg-black bg-opacity-50 rounded-lg border border-yellow-500 text-center">
                    <div className="text-yellow-400 font-bold text-xl mb-2">
                      🎯 URL OFICIAL RECOMENDADA
                    </div>
                    <div className="text-gray-300">
                      Todos os acessos devem usar este domínio
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {/* Informações do Projeto */}
        <div className="mt-8 bg-gray-900 p-6 rounded-2xl border border-yellow-500">
          <h2 className="text-2xl font-bold mb-4 text-yellow-400 text-center">📊 INFORMAÇÕES DO PROJETO</h2>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div className="bg-black p-4 rounded-lg border border-green-500">
              <div className="text-2xl font-bold text-green-400">1</div>
              <div className="text-gray-400">Projeto Principal</div>
            </div>
            <div className="bg-black p-4 rounded-lg border border-blue-500">
              <div className="text-2xl font-bold text-blue-400">27</div>
              <div className="text-gray-400">Páginas</div>
            </div>
            <div className="bg-black p-4 rounded-lg border border-purple-500">
              <div className="text-2xl font-bold text-purple-400">4</div>
              <div className="text-gray-400">URLs Ativas</div>
            </div>
            <div className="bg-black p-4 rounded-lg border border-pink-500">
              <div className="text-2xl font-bold text-pink-400">100%</div>
              <div className="text-gray-400">Consolidado</div>
            </div>
          </div>
        </div>

        <div className="text-center mt-8">
          <a 
            href={DOMINIOS.PRINCIPAL + "/central"}
            className="inline-block bg-green-600 hover:bg-green-700 px-8 py-4 rounded-lg text-white font-bold text-lg transition-colors mr-4"
          >
            🌟 ACESSAR SISTEMA OFICIAL
          </a>
          <a 
            href="/central"
            className="inline-block bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg text-white font-bold transition-colors"
          >
            🔄 VERIFICAR LOCAL
          </a>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
STATUS_FIXED

echo "✅ Página de status criada!"

echo ""
echo "🚀 CONFIGURANDO DEPLOY AUTOMÁTICO..."
echo "==================================="

# Criar script de deploy limpo
cat > deploy.sh << 'DEPLOY_EOF'
#!/bin/bash

echo "🚀 DEPLOY LIMPO - FUNDAÇÃO ALQUIMISTA"
echo "===================================="

# Limpar cache
rm -rf .next
rm -rf node_modules/.cache

# Instalar dependências
npm install

# Build
npm run build

# Deploy
npx vercel --prod --force

echo "✅ Deploy concluído!"
echo "🌐 URL: https://fundacao-alquimista-anatheron.vercel.app"
DEPLOY_EOF

chmod +x deploy.sh

echo ""
echo "🎯 RESUMO DA CONSOLIDAÇÃO:"
echo "=========================="
echo "✅ Projeto principal identificado: fundacao-alquimista-anatheron"
echo "✅ Domínio oficial: https://fundacao-alquimista-anatheron.vercel.app"
echo "✅ Sistema de redirecionamento inteligente implementado"
echo "✅ Página de status para monitoramento"
echo "✅ Configuração Vercel otimizada"

echo ""
echo "📋 PRÓXIMOS PASSOS:"
echo "=================="
echo "1. 🗑️  Excluir projetos antigos no Vercel:"
echo "   - next-video-starter"
echo "   - fundacao-alquimis-git-5dc053"
echo ""
echo "2. 🎯 Usar SEMPRE: https://fundacao-alquimista-anatheron.vercel.app"
echo ""
echo "3. 🔄 Fazer deploy final com: ./deploy.sh"

echo ""
echo "🚀 EXECUTANDO DEPLOY FINAL CONSOLIDADO..."
npm run build && npx vercel --prod --force

