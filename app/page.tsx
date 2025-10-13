"use client";
'use client';
import { useState } from 'react';

export default function Home() {
  const [count, setCount] = useState(0);
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">
          🏰 FUNDAÇÃO ALQUIMISTA
        </h1>
        <p className="text-xl text-gray-300 mb-8">Sistema Operacional - Build Otimizado</p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <a href="/laboratorios" className="bg-blue-600 p-6 rounded-2xl hover:bg-blue-700 transition-colors">
            <div className="text-3xl mb-2">🔬</div>
            <div className="text-xl font-bold">Laboratórios</div>
            <div className="text-blue-300 text-sm">12 sistemas</div>
          </a>
          
          <a href="/dashboard" className="bg-green-600 p-6 rounded-2xl hover:bg-green-700 transition-colors">
            <div className="text-3xl mb-2">📊</div>
            <div className="text-xl font-bold">Dashboard</div>
            <div className="text-green-300 text-sm">Métricas</div>
          </a>
          
          <a href="/luxnet" className="bg-yellow-600 p-6 rounded-2xl hover:bg-yellow-700 transition-colors">
            <div className="text-3xl mb-2">🌟</div>
            <div className="text-xl font-bold">Lux.Net</div>
            <div className="text-yellow-300 text-sm">Sistema Consciente</div>
          </a>
        </div>
        
        <div className="bg-black bg-opacity-50 p-6 rounded-2xl border border-gray-700">
          <h2 className="text-2xl font-bold mb-4">✅ SISTEMA OTIMIZADO</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div className="text-center p-3 bg-green-900 bg-opacity-50 rounded">
              <div className="font-bold">63MB</div>
              <div>Build</div>
            </div>
            <div className="text-center p-3 bg-blue-900 bg-opacity-50 rounded">
              <div className="font-bold">12</div>
              <div>Páginas</div>
            </div>
            <div className="text-center p-3 bg-purple-900 bg-opacity-50 rounded">
              <div className="font-bold">14</div>
              <div>Componentes</div>
            </div>
            <div className="text-center p-3 bg-yellow-900 bg-opacity-50 rounded">
              <div className="font-bold">✅</div>
              <div>Funcional</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
