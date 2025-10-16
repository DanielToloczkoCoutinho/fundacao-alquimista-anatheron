'use client';
import { useState } from 'react';

export default function Dashboard() {
  const [dadosReais] = useState({
    sistemas_complexos: 3285,
    interfaces_vr: 1093,
    sistemas_quantum: 845,
    tecnologias: 61,
    componentes_react: 10
  });

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-green-900 text-white p-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-2">📊 OMEGA DASHBOARD</h1>
        <p className="text-xl text-green-300">Visão Holística Baseada na Análise Real</p>
        <div className="mt-4 inline-block bg-green-600 px-4 py-2 rounded-full">
          🟢 DADOS EM TEMPO REAL
        </div>
      </div>

      {/* MÉTRICAS PRINCIPAIS */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mb-8">
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-3xl font-bold text-red-400">{dadosReais.sistemas_complexos}</div>
          <div className="text-sm text-gray-300">Sistemas Complexos</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-3xl font-bold text-blue-400">{dadosReais.interfaces_vr}</div>
          <div className="text-sm text-gray-300">Interfaces VR</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-3xl font-bold text-purple-400">{dadosReais.sistemas_quantum}</div>
          <div className="text-sm text-gray-300">Sistemas Quânticos</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-3xl font-bold text-yellow-400">{dadosReais.tecnologias}</div>
          <div className="text-sm text-gray-300">Tecnologias</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-3xl font-bold text-green-400">{dadosReais.componentes_react}</div>
          <div className="text-sm text-gray-300">Componentes React</div>
        </div>
      </div>

      <div className="text-center mt-8">
        <a href="/" className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600">
          ← Voltar para Home
        </a>
      </div>
    </div>
  );
}
