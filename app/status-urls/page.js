"use client"

import { useState, useEffect } from 'react'

export default function StatusURLs() {
  const [urls, setUrls] = useState([])
  const [carregando, setCarregando] = useState(true)

  useEffect(() => {
    const verificarURLs = async () => {
      const listaURLs = [
        {
          nome: "🚀 URL DEFINITIVA",
          url: "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app",
          tipo: "definitiva"
        },
        {
          nome: "🔧 URL ALTERNATIVA", 
          url: "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app",
          tipo: "alternativa"
        },
        {
          nome: "📜 URL ANTIGA",
          url: "https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app", 
          tipo: "antiga"
        },
        {
          nome: "🧪 TESTE 1",
          url: "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app",
          tipo: "antiga"
        },
        {
          nome: "🧪 TESTE 2",
          url: "https://fundacao-alquimista-anatheron-oup26gl0o.vercel.app",
          tipo: "antiga" 
        }
      ]

      // Verificar status de cada URL
      const urlsComStatus = await Promise.all(
        listaURLs.map(async (item) => {
          try {
            const response = await fetch(item.url, { method: 'HEAD' })
            return {
              ...item,
              online: response.ok,
              status: response.ok ? 'ONLINE' : 'OFFLINE'
            }
          } catch {
            return {
              ...item,
              online: false,
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
      <div className="max-w-4xl mx-auto">
        
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent">
            🌐 STATUS DAS URLs
          </h1>
          <p className="text-xl text-gray-400">Verificação Completa do Sistema Fundação Alquimista</p>
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
                  item.tipo === 'alternativa' ? 'border-blue-500 bg-blue-900 bg-opacity-20' :
                  'border-gray-500 bg-gray-900 bg-opacity-20'
                }`}
              >
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-white">{item.nome}</h3>
                    <div className="text-gray-400 font-mono text-sm mt-1">{item.url}</div>
                  </div>
                  <div className={`px-3 py-1 rounded-full text-sm font-bold ${
                    item.online ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
                  }`}>
                    {item.status}
                  </div>
                </div>

                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                  <div className={`p-3 rounded-lg ${
                    item.online ? 'bg-green-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Sistema Multiversal</div>
                    <div className={item.online ? 'text-green-400' : 'text-gray-500'}>
                      {item.online ? '✅' : '❌'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.online ? 'bg-blue-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">IA Quântica</div>
                    <div className={item.online ? 'text-blue-400' : 'text-gray-500'}>
                      {item.online ? '✅' : '❌'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.online ? 'bg-purple-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Módulo 29</div>
                    <div className={item.online ? 'text-purple-400' : 'text-gray-500'}>
                      {item.online ? '✅' : '❌'}
                    </div>
                  </div>
                  <div className={`p-3 rounded-lg ${
                    item.online ? 'bg-yellow-900 bg-opacity-30' : 'bg-gray-800'
                  }`}>
                    <div className="text-sm text-gray-400">Completo</div>
                    <div className={item.online ? 'text-yellow-400' : 'text-gray-500'}>
                      {item.online ? '✅' : '❌'}
                    </div>
                  </div>
                </div>

                {item.tipo === 'definitiva' && item.online && (
                  <div className="mt-4 p-3 bg-black bg-opacity-50 rounded-lg border border-yellow-500">
                    <div className="text-yellow-400 font-bold text-center">
                      🎯 URL OFICIAL RECOMENDADA
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        <div className="text-center mt-8">
          <a 
            href="https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app/central"
            className="inline-block bg-green-600 hover:bg-green-700 px-6 py-3 rounded-lg text-white font-bold transition-colors"
          >
            🌟 ACESSAR SISTEMA DEFINITIVO
          </a>
        </div>

      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
