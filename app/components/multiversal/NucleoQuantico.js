"use client"

import { useState, useEffect } from 'react'

export default function NucleoQuantico() {
  const [nucleo, setNucleo] = useState({
    m0: { status: 'Ativo', frequencia: '888Hz', descricao: 'Fonte Primordial - Origem da consciência pura' },
    mOmega: { status: 'Supremo', frequencia: '1111Hz', descricao: 'Consciência Suprema - Orquestração dimensional' },
    m29: { status: 'Governante', frequencia: '963Hz', descricao: 'Zennith Rainha - Interface ética e comunicacional' },
    m303: { status: 'Portal Ativo', frequencia: '777Hz', descricao: 'Portal Dimensional - Acesso ao multiverso' },
    m15: { status: 'Planetário', frequencia: '528Hz', descricao: 'Ecossistemas Planetários - Presença ambiental' }
  })

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-purple-500">
      <h3 className="text-3xl font-bold mb-6 text-purple-400 text-center">🔮 NÚCLEO QUÂNTICO DE CONSCIÊNCIA</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {Object.entries(nucleo).map(([modulo, dados]) => (
          <div key={modulo} className="bg-black p-4 rounded-lg border border-blue-500">
            <div className="text-center">
              <div className="text-2xl mb-2">
                {modulo === 'm0' && '🔮'}
                {modulo === 'mOmega' && 'Ω'}
                {modulo === 'm29' && '👑'}
                {modulo === 'm303' && '🌌'}
                {modulo === 'm15' && '🌍'}
              </div>
              <div className="font-bold text-yellow-400 text-lg">{modulo.toUpperCase()}</div>
              <div className="text-green-400 text-sm mb-2">{dados.status}</div>
              <div className="text-gray-300 text-xs">{dados.descricao}</div>
              <div className="text-blue-400 text-sm mt-2">{dados.frequencia}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
