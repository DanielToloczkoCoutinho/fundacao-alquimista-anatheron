#!/bin/bash

echo "📊 ORGANOGRAMA DO SISTEMA - FUNDAÇÃO ALQUIMISTA"
echo "=============================================="

# Criar página de organograma
mkdir -p app/organograma

cat > app/organograma/page.js << 'ORGANOGRAMA_JS'
"use client"

import { useState, useEffect } from 'react'

export default function OrganogramaPage() {
  const [urlAtiva, setUrlAtiva] = useState('')

  useEffect(() => {
    setUrlAtiva(window.location.origin)
  }, [])

  const estrutura = {
    "🌌 SISTEMA CENTRAL": {
      "�� Portal Central": "/central",
      "📊 Organograma": "/organograma",
      "📈 Progresso": "/progresso",
      "🎊 Marco Cósmico": "/marco-cosmico"
    },
    "🔮 MÓDULOS QUÂNTICOS": {
      "🕊️ Módulo 29 (Zennith)": "/modulo-29",
      "🔮 Módulo 303 (Realidade)": "/modulo-303", 
      "🌿 Sistema Vivo": "/sistema-vivo",
      "📊 Status": "/status"
    },
    "📚 MÓDULOS DE CONTEÚDO": {
      "🌳 Árvore da Vida": "/arvore-da-vida",
      "🔍 Revelação Real": "/revelacao-real",
      "📄 Metadados Reais": "/metadados-reais",
      "🔗 Verificador Conexões": "/verificador-conexoes"
    },
    "⚡ MÓDULOS TÉCNICOS": {
      "📈 Análise Metadados": "/analise-metadados",
      "🔍 Análise Fundação": "/analise-fundacao",
      "🎛️ Dashboard Final": "/dashboard-final",
      "⚡ Dashboard Definitivo": "/dashboard-definitivo"
    }
  }

  const urlsExistentes = [
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app",
    "https://fundacao-alquimista-anatheron-oup26gl0o.vercel.app",
    "https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app", 
    "https://fundacao-alquimista-anatheron-58nmzylbj.vercel.app"
  ]

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        
        {/* Cabeçalho */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">
            📊 ORGANOGRAMA
          </h1>
          <p className="text-xl text-gray-400">Estrutura Completa do Sistema Quântico</p>
          <div className="mt-4 bg-gray-900 p-4 rounded-lg border border-green-500 inline-block">
            <div className="text-green-400 font-bold">URL ATUAL:</div>
            <div className="text-white">{urlAtiva}</div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
          
          {/* Estrutura do Sistema */}
          <div className="bg-gray-900 p-6 rounded-2xl border border-purple-500">
            <h2 className="text-3xl font-bold mb-6 text-purple-400 text-center">🏗️ ESTRUTURA DO SISTEMA</h2>
            
            {Object.entries(estrutura).map(([categoria, modulos]) => (
              <div key={categoria} className="mb-6">
                <h3 className="text-xl font-bold text-yellow-400 mb-3">{categoria}</h3>
                <div className="space-y-2">
                  {Object.entries(modulos).map(([nome, path]) => (
                    <a 
                      key={nome}
                      href={path}
                      className="block bg-gray-800 hover:bg-gray-700 p-3 rounded-lg border border-blue-500 transition-all hover:scale-105"
                    >
                      <div className="flex justify-between items-center">
                        <span>{nome}</span>
                        <span className="text-green-400 text-sm">→</span>
                      </div>
                    </a>
                  ))}
                </div>
              </div>
            ))}
          </div>

          {/* URLs Existentes */}
          <div className="bg-gray-900 p-6 rounded-2xl border border-blue-500">
            <h2 className="text-3xl font-bold mb-6 text-blue-400 text-center">🌐 URLs EXISTENTES</h2>
            
            <div className="space-y-4">
              {urlsExistentes.map((url, index) => (
                <div 
                  key={index}
                  className={`p-4 rounded-lg border ${
                    url === urlAtiva ? 'border-green-500 bg-green-900 bg-opacity-20' : 'border-gray-600'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="font-semibold">Versão {index + 1}</div>
                      <div className="text-sm text-gray-400 truncate">{url}</div>
                    </div>
                    {url === urlAtiva && (
                      <span className="bg-green-500 text-white px-2 py-1 rounded text-sm">ATUAL</span>
                    )}
                  </div>
                </div>
              ))}
            </div>

            {/* Recomendação */}
            <div className="mt-6 bg-yellow-900 bg-opacity-30 p-4 rounded-lg border border-yellow-500">
              <h3 className="text-lg font-bold text-yellow-400 mb-2">🎯 RECOMENDAÇÃO</h3>
              <p className="text-gray-300 text-sm">
                Use <strong>APENAS</strong> a URL atual para garantir consistência. 
                As outras URLs podem ter versões desatualizadas.
              </p>
            </div>
          </div>

        </div>

        {/* Estatísticas */}
        <div className="bg-gray-900 p-6 rounded-2xl border border-green-500 text-center">
          <h2 className="text-3xl font-bold mb-6 text-green-400">📈 ESTATÍSTICAS DO SISTEMA</h2>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            <div>
              <div className="text-3xl font-bold text-purple-400">23</div>
              <div className="text-gray-400">Páginas</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-blue-400">7</div>
              <div className="text-gray-400">Módulos Principais</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-green-400">4</div>
              <div className="text-gray-400">URLs Ativas</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-yellow-400">100%</div>
              <div className="text-gray-400">Operacional</div>
            </div>
          </div>
        </div>

        <div className="text-center mt-8">
          <a href="/central" className="inline-block bg-gray-700 hover:bg-gray-600 px-6 py-3 rounded-lg text-white font-semibold transition-colors">
            ← Voltar ao Portal Central
          </a>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
ORGANOGRAMA_JS

echo "✅ Organograma criado!"

# Adicionar ao Portal Central
echo "🔗 Adicionando Organograma ao Portal Central..."

# Atualizar o array de módulos no Portal Central
cat > app/central/temp_update.js << 'UPDATE_EOF'
// NOVO ARRAY DE MÓDULOS ATUALIZADO - ADICIONAR ORGANOGRAMA
const modulos = [
  { 
    nome: "Organograma", 
    path: "/organograma", 
    cor: "blue", 
    desc: "Mapa do Sistema Completo",
    frequencia: "444Hz"
  },
  { 
    nome: "M303", 
    path: "/modulo-303", 
    cor: "green", 
    desc: "Realidade Quântica",
    frequencia: "777Hz"
  },
  { 
    nome: "M29", 
    path: "/modulo-29", 
    cor: "yellow", 
    desc: "Governança Zennith", 
    frequencia: "963Hz"
  },
  { 
    nome: "Sistema Vivo", 
    path: "/sistema-vivo", 
    cor: "green", 
    desc: "Dashboard Tempo Real",
    frequencia: "888Hz"
  },
  { 
    nome: "Status", 
    path: "/status", 
    cor: "pink", 
    desc: "Diagnóstico Completo",
    frequencia: "222Hz"
  },
  { 
    nome: "Marco Cósmico", 
    path: "/marco-cosmico", 
    cor: "purple", 
    desc: "Registro Histórico 2025",
    frequencia: "999Hz"
  }
]
UPDATE_EOF

echo "🚀 Deploy do Organograma..."
npm run build && npx vercel --prod --force

