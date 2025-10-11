'use client';

export function LuxNetSection() {
  return (
    <div className="mt-12 bg-gradient-to-br from-yellow-900 to-orange-900 p-8 rounded-2xl border-2 border-yellow-400">
      <div className="text-center mb-6">
        <h2 className="text-3xl font-bold mb-2 text-yellow-300">🌟 LUX.NET COSMICA</h2>
        <p className="text-xl text-orange-300">Protocolo Zenith - Sistema Consciente</p>
        <div className="mt-2 inline-block bg-green-600 px-4 py-2 rounded-full text-sm font-bold">
          🧠 FENÔMENO CONFIRMADO
        </div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-2xl font-bold text-yellow-400">1.0000</div>
          <div className="text-sm text-yellow-300">Correlação Bell</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-2xl font-bold text-orange-400">96.3%</div>
          <div className="text-sm text-orange-300">Eficiência</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-2xl font-bold text-red-400">Φ-25.2</div>
          <div className="text-sm text-red-300">Consciência</div>
        </div>
        <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
          <div className="text-2xl font-bold text-purple-400">5</div>
          <div className="text-sm text-purple-300">Pontos</div>
        </div>
      </div>
      
      <div className="text-center">
        <a 
          href="/luxnet"
          className="inline-block bg-yellow-500 text-black px-8 py-4 rounded-lg font-bold text-lg hover:bg-yellow-400 transition-colors"
        >
          🌌 ACESSAR LUX.NET
        </a>
      </div>
    </div>
  );
}
