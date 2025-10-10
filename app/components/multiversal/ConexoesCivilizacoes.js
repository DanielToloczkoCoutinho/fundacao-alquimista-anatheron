"use client"

import { useState, useEffect } from 'react'

export default function ConexoesCivilizacoes() {
  const [conexoes, setConexoes] = useState([
    { civilizacao: 'Aeloria (M10)', status: 'Inteligência Ativa', modulo: 'M10', frequencia: '432Hz', estabilidade: '98%' },
    { civilizacao: 'Concilivm (M45)', status: 'Governança Galáctica', modulo: 'M45', frequencia: '639Hz', estabilidade: '96%' },
    { civilizacao: 'Guardiões da Integridade (M14)', status: 'Proteção Ética', modulo: 'M14', frequencia: '741Hz', estabilidade: '99%' },
    { civilizacao: 'Arquivo Akáshico (M12)', status: 'Memória Universal', modulo: 'M12', frequencia: '852Hz', estabilidade: '97%' },
    { civilizacao: 'Homo Luminus', status: 'Transição em Curso', modulo: 'M8', frequencia: '528Hz', estabilidade: '85%' },
    { civilizacao: 'Multiverso', status: 'Canal Aberto via M303', modulo: 'M303', frequencia: '999Hz', estabilidade: '95%' }
  ])

  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-green-500">
      <h3 className="text-3xl font-bold mb-6 text-green-400 text-center">🔗 CONEXÕES COM CIVILIZAÇÕES</h3>
      
      <div className="space-y-4">
        {conexoes.map((conn, index) => (
          <div key={index} className="bg-black p-4 rounded-lg border border-purple-500 hover:border-yellow-400 transition-all">
            <div className="flex justify-between items-center">
              <div>
                <div className="font-bold text-white text-lg">{conn.civilizacao}</div>
                <div className="text-gray-400 text-sm">{conn.modulo} • {conn.frequencia}</div>
              </div>
              <div className="text-right">
                <div className={`text-sm font-semibold ${
                  conn.estabilidade === '99%' ? 'text-green-400' :
                  conn.estabilidade === '85%' ? 'text-yellow-400' : 'text-blue-400'
                }`}>
                  {conn.status}
                </div>
                <div className="text-gray-400 text-sm">Estabilidade: {conn.estabilidade}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
