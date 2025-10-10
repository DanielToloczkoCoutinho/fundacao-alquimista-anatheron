"use client"

import { useState, useEffect } from 'react'

export default function Modulo303() {
  const [dados, setDados] = useState({
    frequencia: "777.0 Hz",
    coerencia: "95.5%",
    circuitos: 1331,
    temperatura: "0.00256K",
    dimensoes: "12/12 Ativas"
  })
  const [scans, setScans] = useState([])
  const [contador, setContador] = useState(0)
  const [animacaoAtiva, setAnimacaoAtiva] = useState(true)

  useEffect(() => {
    console.log('🔮 Módulo 303 - Simulação dimensional iniciada...')
    
    const interval = setInterval(() => {
      setContador(prev => prev + 1)
      
      // Atualização de dados em tempo real
      setDados(prev => ({
        frequencia: `${(777 + Math.random() * 10).toFixed(1)} Hz`,
        coerencia: `${(95 + Math.random() * 3).toFixed(1)}%`,
        circuitos: 1331 + Math.floor(Math.random() * 10),
        temperatura: `${(0.00256 + Math.random() * 0.0001).toFixed(5)}K`,
        dimensoes: "12/12 Ativas"
      }))

      // Scanner dimensional - a cada 3 ciclos
      if (contador % 3 === 0) {
        const dimensoes = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12']
        const atividades = ['Estável', 'Oscilando', 'Harmonioso', 'Resonante', 'Coerente']
        
        setScans(prev => [{
          id: Date.now(),
          timestamp: new Date().toLocaleTimeString(),
          dimensao: dimensoes[Math.floor(Math.random() * dimensoes.length)],
          estabilidade: `${(85 + Math.random() * 15).toFixed(1)}%`,
          atividade: atividades[Math.floor(Math.random() * atividades.length)],
          frequencia: `${(100 + Math.random() * 900).toFixed(0)}Hz`
        }, ...prev.slice(0, 8)])
      }
    }, 1500)

    return () => clearInterval(interval)
  }, [contador])

  const toggleAnimacao = () => {
    setAnimacaoAtiva(!animacaoAtiva)
  }

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            🔮 MÓDULO 303
          </h1>
          <p className="text-xl text-gray-400 mb-4">Interface de Simulação Dimensional</p>
          <div className="flex justify-center space-x-4 mb-4">
            <span className="text-green-400 text-sm">● SIMULAÇÃO ATIVA</span>
            <span className="text-gray-400">|</span>
            <span className="text-blue-400 text-sm">Ciclo: {contador}</span>
            <span className="text-gray-400">|</span>
            <button 
              onClick={toggleAnimacao}
              className="text-yellow-400 text-sm hover:underline"
            >
              {animacaoAtiva ? '⏸️ Pausar' : '▶️ Retomar'}
            </button>
          </div>
        </div>

        {/* Painel de Métricas em Tempo Real */}
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-8">
          <div className="bg-gray-900 p-4 rounded-xl border border-purple-500 text-center">
            <div className={`text-2xl font-bold text-purple-400 ${animacaoAtiva ? 'animate-pulse' : ''}`}>
              {dados.frequencia}
            </div>
            <div className="text-sm text-gray-400 mt-1">Frequência</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-xl border border-green-500 text-center">
            <div className={`text-2xl font-bold text-green-400 ${animacaoAtiva ? 'animate-pulse' : ''}`}>
              {dados.coerencia}
            </div>
            <div className="text-sm text-gray-400 mt-1">Coerência</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-xl border border-blue-500 text-center">
            <div className="text-2xl font-bold text-blue-400">{dados.circuitos}</div>
            <div className="text-sm text-gray-400 mt-1">Circuitos</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-xl border border-red-500 text-center">
            <div className="text-2xl font-bold text-red-400">{dados.temperatura}</div>
            <div className="text-sm text-gray-400 mt-1">Temperatura</div>
          </div>
          <div className="bg-gray-900 p-4 rounded-xl border border-yellow-500 text-center">
            <div className="text-2xl font-bold text-yellow-400">{dados.dimensoes}</div>
            <div className="text-sm text-gray-400 mt-1">Dimensões</div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Scanner Dimensional */}
          <div className="bg-gray-900 p-6 rounded-xl border border-blue-500">
            <h3 className="text-xl font-bold mb-4 text-blue-400 flex items-center">
              📡 SCANNER DIMENSIONAL
              <span className="ml-2 text-green-400 text-sm">● ATIVO</span>
            </h3>
            <div className="h-80 overflow-y-auto bg-black rounded-lg p-4">
              <div className="grid grid-cols-5 gap-2 text-xs text-gray-400 mb-2 font-semibold">
                <span>HORA</span>
                <span>DIMENSÃO</span>
                <span>ESTABILIDADE</span>
                <span>ESTADO</span>
                <span>FREQ</span>
              </div>
              {scans.map(scan => (
                <div key={scan.id} className="grid grid-cols-5 gap-2 text-sm mb-2 py-1 border-b border-gray-800">
                  <span className="text-gray-400 text-xs">{scan.timestamp.split(' ')[1]}</span>
                  <span className="text-purple-400 font-mono">{scan.dimensao}</span>
                  <span className={
                    parseFloat(scan.estabilidade) > 90 ? "text-green-400" :
                    parseFloat(scan.estabilidade) > 80 ? "text-yellow-400" : "text-red-400"
                  }>
                    {scan.estabilidade}
                  </span>
                  <span className={
                    scan.atividade === 'Estável' ? 'text-green-400' :
                    scan.atividade === 'Harmonioso' ? 'text-blue-400' :
                    scan.atividade === 'Resonante' ? 'text-purple-400' : 'text-yellow-400'
                  }>
                    {scan.atividade}
                  </span>
                  <span className="text-orange-400 font-mono">{scan.frequencia}</span>
                </div>
              ))}
              {scans.length === 0 && (
                <div className="text-gray-500 text-center py-12">
                  <div className="text-4xl mb-2">🌌</div>
                  <div>Inicializando scanner dimensional...</div>
                </div>
              )}
            </div>
          </div>

          {/* Visualização Holográfica */}
          <div className="bg-gray-900 p-6 rounded-xl border border-purple-500">
            <h3 className="text-xl font-bold mb-4 text-purple-400">👁️ VISUALIZAÇÃO HOLOGRÁFICA</h3>
            <div className="h-80 bg-gradient-to-br from-purple-900 via-black to-blue-900 rounded-lg flex items-center justify-center relative overflow-hidden">
              {/* Animação de partículas */}
              <div className="absolute inset-0 opacity-30">
                <div className="absolute top-1/4 left-1/4 w-2 h-2 bg-purple-400 rounded-full animate-ping"></div>
                <div className="absolute top-1/3 right-1/3 w-1 h-1 bg-blue-400 rounded-full animate-pulse"></div>
                <div className="absolute bottom-1/4 left-1/2 w-3 h-3 bg-pink-400 rounded-full animate-bounce"></div>
                <div className="absolute top-1/2 right-1/4 w-1 h-1 bg-green-400 rounded-full animate-pulse"></div>
              </div>
              
              <div className="text-center z-10">
                <div className="text-6xl mb-4">🌐</div>
                <div className="text-xl font-bold text-white mb-2">REALIDADE QUÂNTICA</div>
                <div className="text-gray-400 text-sm">
                  {animacaoAtiva ? 'Simulação em tempo real' : 'Simulação pausada'}
                </div>
                <div className="mt-4 text-xs text-gray-500">
                  Dimensões: {dados.dimensoes} | Ciclo: {contador}
                </div>
              </div>
            </div>
            
            <div className="mt-4 grid grid-cols-2 gap-2 text-sm">
              <button className="bg-purple-600 hover:bg-purple-700 py-2 rounded transition-colors">
                🔄 Reiniciar Scanner
              </button>
              <button className="bg-blue-600 hover:bg-blue-700 py-2 rounded transition-colors">
                📊 Exportar Dados
              </button>
            </div>
          </div>
        </div>

        <div className="mt-8 text-center">
          <a href="/central" className="inline-block bg-gray-700 hover:bg-gray-600 px-6 py-3 rounded-lg text-white font-semibold transition-colors">
            ← Voltar ao Portal Central
          </a>
        </div>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
