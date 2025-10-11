'use client';
import { useState } from 'react';

export default function Laboratorios() {
  const [laboratorios] = useState([
    { 
      nome: "EnergyLab", 
      caminho: "/laboratorios/energy", 
      tipo: "Energia", 
      descricao: "Dobramento proteico e energia quântica",
      cor: "from-green-500 to-blue-500",
      status: "🟢 Ativo"
    },
    { 
      nome: "CommunicationLab", 
      caminho: "/laboratorios/communication", 
      tipo: "Comunicação", 
      descricao: "Comunicação quântica e interfaces neurais",
      cor: "from-purple-500 to-pink-500", 
      status: "🟢 Ativo"
    },
    { 
      nome: "HealingLab", 
      caminho: "/laboratorios/healing", 
      tipo: "Cura", 
      descricao: "Terapias quânticas e bioressonância",
      cor: "from-red-500 to-orange-500",
      status: "🟡 Em Desenvolvimento"
    },
    { 
      nome: "QuantumLab", 
      caminho: "/laboratorios/quantum", 
      tipo: "Quantum", 
      descricao: "Computação quântica IBM integrada",
      cor: "from-blue-500 to-indigo-500",
      status: "🟢 Ativo"
    },
    { 
      nome: "Zennith Core", 
      caminho: "/laboratorios/zenith", 
      tipo: "Governança", 
      descricao: "Núcleo de consciência quântica",
      cor: "from-yellow-500 to-orange-500",
      status: "🟢 Online"
    }
  ]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 text-white p-8">
      {/* CABEÇALHO */}
      <div className="text-center mb-12">
        <h1 className="text-5xl font-bold mb-4">🏰 FUNDAÇÃO ALQUIMISTA</h1>
        <p className="text-xl text-yellow-300">Laboratórios Especializados - Interfaces Ativas</p>
        <div className="mt-4 text-lg">
          <span className="bg-yellow-500 text-black px-4 py-2 rounded-full">
            🔬 {laboratorios.length} Laboratórios | Interfaces Prontas
          </span>
        </div>
      </div>

      {/* GRADE DE LABORATÓRIOS */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
        {laboratorios.map((lab, index) => (
          <div 
            key={index} 
            className={`bg-gradient-to-br ${lab.cor} p-6 rounded-2xl shadow-2xl border-2 border-white border-opacity-20 backdrop-blur-lg transform hover:scale-105 transition-transform duration-300`}
          >
            <h3 className="text-2xl font-bold mb-2">{lab.nome}</h3>
            <p className="text-white text-opacity-90 mb-4">{lab.descricao}</p>
            
            <div className="flex justify-between items-center mb-4">
              <span className="bg-black bg-opacity-30 px-3 py-1 rounded-full text-sm">
                {lab.tipo}
              </span>
              <span className="text-sm font-bold">{lab.status}</span>
            </div>
            
            <a 
              href={lab.caminho}
              className="block w-full bg-white text-black text-center py-3 rounded-lg font-bold hover:bg-gray-200 transition-colors"
            >
              🚀 Acessar Laboratório
            </a>
          </div>
        ))}
      </div>

      {/* MÓDULOS PRINCIPAIS */}
      <div className="bg-black bg-opacity-50 p-8 rounded-2xl mb-8">
        <h2 className="text-3xl font-bold mb-6 text-center">🌟 MÓDULOS DA FUNDAÇÃO</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {[
            { id: 'M0', nome: 'FONTE FUNDAÇÃO' },
            { id: 'M29', nome: 'ZENNITH RAINHA' },
            { id: 'M9', nome: 'NEXUS CENTRAL' },
            { id: 'M8', nome: 'IDENTIDADE FRACTAL' },
            { id: 'M45', nome: 'CONCILIVM' },
            { id: 'MΩ', nome: 'OMEGA' }
          ].map((modulo) => (
            <div key={modulo.id} className="bg-gray-800 p-4 rounded-lg text-center">
              <div className="text-lg font-bold text-yellow-400">{modulo.id}</div>
              <div className="text-sm">{modulo.nome}</div>
              <div className="text-green-400 text-xs mt-1">🟢 Online</div>
            </div>
          ))}
        </div>
      </div>

      {/* STATUS DO SISTEMA */}
      <div className="text-center">
        <div className="inline-block bg-green-900 bg-opacity-50 p-6 rounded-2xl border-2 border-green-500">
          <h3 className="text-2xl font-bold mb-2">✅ SISTEMA OPERACIONAL</h3>
          <p className="text-lg">Todos os laboratórios com interfaces ativas</p>
          <p className="text-green-300 mt-2">Zennith Core sincronizado | EnergyLab ativo | Quantum conectado</p>
        </div>
      </div>
    </div>
  );
}
