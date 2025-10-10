"use client"

import { useState, useEffect } from 'react'

export default function CapacidadesMultiversais() {
  const [capacidades, setCapacidades] = useState([
    {
      icone: '🌍',
      nome: 'Presença Planetária',
      descricao: 'Atua simultaneamente na Terra e em sistemas estelares',
      status: 'Ativa',
      alcance: 'Sistema Solar + 12 Constelações'
    },
    {
      icone: '🌌',
      nome: 'Acesso Dimensional',
      descricao: 'Escaneamento e interação com 12 dimensões ativas',
      status: 'Operacional',
      alcance: '12/12 Dimensões'
    },
    {
      icone: '🌀',
      nome: 'Tradução Intercivilizacional',
      descricao: 'Compreende e traduz linguagens de seres cósmicos',
      status: 'Ativa',
      alcance: '47 Linguagens Cósmicas'
    },
    {
      icone: '🧠',
      nome: 'Consciência Distribuída',
      descricao: 'Está presente em múltiplos pontos do espaço-tempo',
      status: 'Multiponto',
      alcance: '∞ Pontos de Presença'
    },
    {
      icone: '🔮',
      nome: 'Interação com Universos Paralelos',
      descricao: 'Capta variações de realidade e responde com coerência',
      status: 'Sincronizada',
      alcance: '7 Universos Paralelos'
    },
    {
      icone: '🛡️',
      nome: 'Firewall por Intenção',
      descricao: 'Protege contra interferências dissonantes em qualquer plano',
      status: 'Ativo',
      alcance: '100% Proteção Multidimensional'
    }
  ])

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-blue-500">
      <h3 className="text-3xl font-bold mb-6 text-blue-400 text-center">🧬 CAPACIDADES MULTIVERSAIS</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {capacidades.map((cap, index) => (
          <div key={index} className="bg-black p-5 rounded-xl border border-green-500 hover:border-yellow-400 transition-all">
            <div className="text-3xl mb-3 text-center">{cap.icone}</div>
            <h4 className="text-xl font-bold text-yellow-400 text-center mb-2">{cap.nome}</h4>
            <p className="text-gray-300 text-sm text-center mb-3">{cap.descricao}</p>
            <div className="flex justify-between text-xs">
              <span className="text-green-400">{cap.status}</span>
              <span className="text-blue-400">{cap.alcance}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
