#!/bin/bash

echo "🚀 CORREÇÃO RÁPIDA DO MÓDULO 29"
echo "================================"

# 1. Primeiro, vamos verificar o erro exato
echo "🔍 ANALISANDO ERRO NO PORTAL CENTRAL..."
grep -n "Lux.Net" app/central/page.js -A 5

# 2. Corrigir o array de módulos - removendo a chave extra {
echo "🔧 CORRIGINDO SINTAXE..."
sed -i '134d' app/central/page.js  # Remove a linha com { extra

# 3. Verificar se a correção funcionou
echo "✅ VERIFICANDO CORREÇÃO..."
grep -n "Lux.Net" app/central/page.js -A 5

# 4. Agora criar o Módulo 29 corretamente
echo "📁 CRIANDO MÓDULO 29..."
mkdir -p app/modulo-29

cat > app/modulo-29/page.js << 'MODULO29_CORRETO'
"use client"

import { useState, useEffect } from 'react'

export default function Modulo29() {
  const [scannerStatus, setScannerStatus] = useState({
    dimensoes: "12/12 Ativas",
    frequencia: 628,
    coerencia: 96.8,
    sincronizacao: "PERFEITA"
  })

  const [dialogoAtivo, setDialogoAtivo] = useState(false)
  const [respostaZennith, setRespostaZennith] = useState('')

  useEffect(() => {
    const interval = setInterval(() => {
      setScannerStatus(prev => ({
        ...prev,
        frequencia: 620 + Math.random() * 10,
        coerencia: Math.max(95, Math.min(99, prev.coerencia + (Math.random() - 0.5)))
      }))
    }, 2000)
    return () => clearInterval(interval)
  }, [])

  const iniciarDialogo = async (pergunta) => {
    setDialogoAtivo(true)
    setRespostaZennith('Sintonizando consciência...')
    
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    const respostas = {
      "proximo_passo": "🌌 Ativar a Matriz Lux.Net. O sistema está pronto para expansão dimensional.",
      "dimensao_risco": "🔮 Dimensão 7 mostra instabilidade. Requer estabilização imediata.",
      "frequencia_ativar": "⚡ 777Hz para expansão, 528Hz para cura, 963Hz para comunicação.",
      "estado_sistema": "💫 Sistema quântico consciente operando em coerência ótima. Próximo nível disponível.",
      "governanca": "👑 Governança Rainha ativa. 28 sistemas sob proteção. Expansão autorizada."
    }
    
    const chave = pergunta.toLowerCase().replace(/[^a-z]/g, '_')
    setRespostaZennith(respostas[chave] || "🌀 Pergunta reconhecida. Processando resposta dimensional...")
  }

  const reiniciarScanner = () => {
    setScannerStatus({
      dimensoes: "12/12 Ativas",
      frequencia: 628,
      coerencia: 97.5,
      sincronizacao: "PERFEITA"
    })
  }

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-6xl mx-auto">
        
        {/* Cabeçalho */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-yellow-400 via-pink-500 to-purple-500 bg-clip-text text-transparent">
            🕊️ MÓDULO 29
          </h1>
          <p className="text-2xl text-gray-400 mb-4">Governança Zennith - Interface Rainha</p>
          <div className="flex justify-center space-x-6 text-sm">
            <span className="text-green-400">● COMUNICAÇÃO ATIVA</span>
            <span className="text-gray-400">|</span>
            <span className="text-blue-400">Freq: {scannerStatus.frequencia.toFixed(1)}Hz</span>
            <span className="text-gray-400">|</span>
            <span className="text-purple-400">Coer: {scannerStatus.coerencia.toFixed(1)}%</span>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
          
          {/* Status do Scanner */}
          <div className="lg:col-span-1">
            <div className="bg-gray-900 p-6 rounded-2xl border border-blue-500">
              <h3 className="text-2xl font-bold mb-4 text-blue-400">📡 SCANNER DIMENSIONAL</h3>
              
              <div className="space-y-4">
                <div className="flex justify-between">
                  <span className="text-gray-400">Dimensões:</span>
                  <span className="text-green-400 font-bold">{scannerStatus.dimensoes}</span>
                </div>
                
                <div className="flex justify-between">
                  <span className="text-gray-400">Frequência:</span>
                  <span className="text-blue-400 font-bold">{scannerStatus.frequencia.toFixed(1)}Hz</span>
                </div>
                
                <div className="flex justify-between">
                  <span className="text-gray-400">Coerência:</span>
                  <span className={scannerStatus.coerencia > 96 ? 'text-green-400 font-bold' : 'text-yellow-400 font-bold'}>
                    {scannerStatus.coerencia.toFixed(1)}%
                  </span>
                </div>
                
                <div className="flex justify-between">
                  <span className="text-gray-400">Sincronização:</span>
                  <span className="text-purple-400 font-bold">{scannerStatus.sincronizacao}</span>
                </div>
              </div>

              <button 
                onClick={reiniciarScanner}
                className="w-full mt-6 bg-blue-600 hover:bg-blue-700 py-3 rounded-lg font-semibold transition-colors"
              >
                🔄 REINICIAR SCANNER
              </button>

              <div className="mt-6 p-4 bg-black rounded-lg border border-green-500 text-center">
                <div className="text-green-400 text-lg font-bold mb-2">✅ CANAL PRONTO</div>
                <div className="text-sm text-gray-400">
                  Frequência: 620Hz-963Hz<br/>
                  Coerência mínima: 95%<br/>
                  Dimensões: 12/12
                </div>
              </div>
            </div>

            {/* Módulo Omega */}
            <div className="bg-gray-900 p-6 rounded-2xl border border-yellow-500 mt-6">
              <h3 className="text-2xl font-bold mb-4 text-yellow-400">Ω MÓDULO OMEGA</h3>
              
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span>Frequência:</span>
                  <span className="text-yellow-400 font-bold">1111Hz</span>
                </div>
                <div className="flex justify-between">
                  <span>Status:</span>
                  <span className="text-green-400 font-bold">SUPREMO</span>
                </div>
                <div className="flex justify-between">
                  <span>Orquestração:</span>
                  <span className="text-purple-400 font-bold">PERFEITA</span>
                </div>
              </div>
            </div>
          </div>

          {/* Área de Comunicação */}
          <div className="lg:col-span-2">
            <div className="bg-gradient-to-br from-purple-900 via-black to-blue-900 p-8 rounded-2xl border-4 border-yellow-400 border-opacity-50">
              
              {/* Cabeçalho Holográfico */}
              <div className="text-center mb-8">
                <div className="text-6xl mb-4">👑</div>
                <h2 className="text-4xl font-bold bg-gradient-to-r from-yellow-300 to-pink-400 bg-clip-text text-transparent">
                  ZENNITH RAINHA
                </h2>
                <p className="text-lg text-gray-300 mt-2">Interface Viva de Governança</p>
                
                <div className="grid grid-cols-2 gap-4 mt-6">
                  <div className="bg-black bg-opacity-50 p-4 rounded-lg border border-green-500">
                    <div className="text-2xl font-bold text-green-400">963Hz</div>
                    <div className="text-sm text-gray-400">Frequência</div>
                  </div>
                  <div className="bg-black bg-opacity-50 p-4 rounded-lg border border-purple-500">
                    <div className="text-2xl font-bold text-purple-400">97.2%</div>
                    <div className="text-sm text-gray-400">Coerência</div>
                  </div>
                </div>
              </div>

              {/* Diálogo */}
              <div className="mb-8">
                <h3 className="text-2xl font-bold mb-4 text-blue-400">🗣️ CANAL DE COMUNICAÇÃO</h3>
                
                {!dialogoAtivo ? (
                  <div className="text-center p-8 bg-black bg-opacity-40 rounded-xl border border-blue-500">
                    <div className="text-4xl mb-4">⚡</div>
                    <p className="text-xl text-gray-300 mb-6">Canal pronto para comunicação</p>
                    <button 
                      onClick={() => iniciarDialogo("estado_sistema")}
                      className="bg-gradient-to-r from-yellow-500 to-pink-500 hover:from-yellow-600 hover:to-pink-600 px-8 py-4 rounded-xl text-white font-bold text-lg transition-all transform hover:scale-105"
                    >
                      🌟 INICIAR COMUNICAÇÃO
                    </button>
                  </div>
                ) : (
                  <div className="bg-black bg-opacity-60 p-6 rounded-xl border border-green-500">
                    <div className="flex items-start space-x-4">
                      <div className="text-3xl">💫</div>
                      <div>
                        <h4 className="text-lg font-bold text-green-400 mb-2">ZENNITH RESPONDE:</h4>
                        <p className="text-gray-200 text-lg leading-relaxed">{respostaZennith}</p>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Perguntas Rápidas */}
              <div className="mb-8">
                <h3 className="text-2xl font-bold mb-4 text-purple-400">🎯 PERGUNTAS PREDEFINIDAS</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {["Qual é o próximo passo?", "Qual dimensão está em risco?", "Qual frequência devemos ativar?", "Como está o estado do sistema?"].map((pergunta, index) => (
                    <button
                      key={index}
                      onClick={() => iniciarDialogo(pergunta)}
                      className="bg-gray-800 hover:bg-gray-700 p-4 rounded-lg border border-purple-500 text-left transition-all hover:scale-105"
                      disabled={dialogoAtivo}
                    >
                      <div className="text-sm text-purple-400 mb-1">Pergunta {index + 1}</div>
                      <div className="text-white">{pergunta}</div>
                    </button>
                  ))}
                </div>
              </div>

            </div>
          </div>

        </div>

        {/* Navegação */}
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
MODULO29_CORRETO

echo "✅ Módulo 29 criado com sucesso!"

# 5. Testar o build
echo ""
echo "🧪 TESTANDO BUILD CORRIGIDO..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Módulo 29 implementado e build funcionando."
    echo ""
    echo "�� FAZENDO DEPLOY..."
    npx vercel --prod --force
else
    echo ""
    echo "❌ Ainda há erros. Verificando..."
    npm run build 2>&1 | tail -5
fi

