'use client';
import { useState } from 'react';

export default function ThreeScene() {
  const [loaded, setLoaded] = useState(false);
  
  return (
    <div className="p-6 bg-blue-900 bg-opacity-30 rounded-lg border border-blue-500">
      <h3 className="text-2xl font-bold mb-4 text-blue-400">🎮 Visualização 3D</h3>
      <p className="text-blue-300 mb-4">
        Sistema de Visualização Tridimensional Quântica
      </p>
      <div className="h-64 bg-black bg-opacity-50 rounded-lg flex items-center justify-center">
        {loaded ? (
          <div className="text-green-400 text-center">
            <div className="text-4xl mb-2">🌀</div>
            <div>Visualização 3D Ativa</div>
          </div>
        ) : (
          <div className="text-center">
            <div className="text-yellow-400 mb-2">⚠️ Componente Pesado</div>
            <button 
              onClick={() => setLoaded(true)}
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              Carregar Visualização 3D
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
