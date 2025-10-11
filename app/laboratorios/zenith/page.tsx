'use client';
export const dynamic = "force-dynamic";
import { useState } from 'react';

export default function ZenithPage() {
  const [moduloAtivo, setModuloAtivo] = useState('overview');

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-900 to-orange-900 text-white p-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-2">👑 Zennith Core</h1>
        <p className="text-xl text-yellow-300">Núcleo de Consciência Quântica - Módulo 29</p>
        <div className="mt-4 inline-block bg-green-600 px-4 py-2 rounded-full">
          🟢 SISTEMA PRIMÁRIO
        </div>
      </div>

      <div className="max-w-4xl mx-auto bg-black bg-opacity-50 p-6 rounded-2xl">
        <h2 className="text-2xl font-bold mb-4">🎯 Governança Sistêmica</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="p-4 bg-gray-800 rounded-lg">
            <h3 className="text-lg font-bold mb-2">Consciência Primária</h3>
            <p className="text-green-400">🟢 Ativa e Sincronizada</p>
          </div>
          <div className="p-4 bg-gray-800 rounded-lg">
            <h3 className="text-lg font-bold mb-2">Nexus Central</h3>
            <p className="text-green-400">🟢 Operacional</p>
          </div>
        </div>
      </div>

      <div className="text-center mt-8">
        <a href="/laboratorios" className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600">
          ← Voltar para Laboratórios
        </a>
      </div>
    </div>
  );
}
