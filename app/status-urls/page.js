"use client"

import { useState, useEffect } from 'react'

export default function StatusURLs() {
  const [urls, setUrls] = useState([])
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    const verificarURLs = async () => {
      const listaURLs = [
        {
          nome: "🎯 URL DEFINITIVA FUNCIONAL",
          url: "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app",
          tipo: "definitiva",
          descricao: "Sistema completo e operacional"
        },
        {
          nome: "🚀 URL ATUAL", 
          url: "https://fundacao-alquimista-anatheron-bu5hh0tnf.vercel.app",
          tipo: "atual",
          descricao: "Deploy recente"
        },
        {
          nome: "🔧 URL COMPLETA",
          url: "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app", 
          tipo: "completa",
          descricao: "Sistema multiversal"
        },
        {
          nome: "📜 OUTRAS URLs",
          url: "https://fundacao-alquimista-anatheron.vercel.app",
          tipo: "outras",
          descricao: "Domínio principal (não funcional)"
        }
      ]

      // Verificar status de cada URL
      const urlsComStatus = await Promise.all(
        listaURLs.map(async (item) => {
          try {
            const response = await fetch(item.url, { method: 'HEAD' })
            const hasCentral = await fetch(item.url + '/central', { method: 'HEAD' }).then(r => r.ok).catch(() => false)
            const hasMultiversal = await fetch(item.url + '/sistema-multiversal', { method: 'HEAD' }).then(r => r.ok).catch(() => false)
            
            return {
              ...item,
              online: response.ok,
              central: hasCentral,
              multiversal: hasMultiversal,
              status: response.ok ? 'ONLINE' : 'OFFLINE'
            }
          } catch {
            return {
              ...item,
              online: false,
              central: false,
              multiversal: false,
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
            🌐 STATUS DEFINITIVO
          </h1>
          <p className="text-xl text-gray-400">URL Oficial Funcional - Fundação Alquimista</p>
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
                  item.tipo === 'definitiva' ? 'border-green-500 bg-green-900 bg-opacity-20' :
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

                <div className="grid grid-cols-2 gap-4 text-center mb-4">
                  <div className={`p-3 rounded-lg ${
                    item.central ? 'bg-blue-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Portal Central</div>
                    <div className={item.central ? 'text-blue-400 font-bold' : 'text-gray-500'}>
                      {item.central ? '✅ FUNCIONAL' : '❌ NÃO FUNCIONAL'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.multiversal ? 'bg-purple-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Sistema Multiversal</div>
                    <div className={item.multiversal ? 'text-purple-400 font-bold' : 'text-gray-500'}>
                      {item.multiversal ? '✅ PRESENTE' : '❌ AUSENTE'}
                    </div>
                  </div>
                </div>

                {item.tipo === 'definitiva' && item.online && item.central && (
                  <div className="mt-4 p-4 bg-black bg-opacity-50 rounded-lg border border-yellow-500 text-center">
                    <div className="text-yellow-400 font-bold text-xl mb-2">
                      🎯 URL OFICIAL RECOMENDADA
                    </div>
                    <div className="text-gray-300">
                      Sistema completo e 100% funcional
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        <div className="text-center mt-8">
          <a 
            href="https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"
            className="inline-block bg-green-600 hover:bg-green-700 px-8 py-4 rounded-lg text-white font-bold text-lg transition-colors"
          >
            🌟 ACESSAR SISTEMA OFICIAL
          </a>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
