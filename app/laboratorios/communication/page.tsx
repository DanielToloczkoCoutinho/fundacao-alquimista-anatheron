"use client";
export default function CommunicationLabPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-900 text-white p-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-2">📡 CommunicationLab</h1>
        <p className="text-xl text-purple-300">Sistema de Comunicação Quântica</p>
        <div className="mt-4 inline-block bg-green-600 px-4 py-2 rounded-full">
          🟢 SISTEMA ATIVO
        </div>
      </div>

      <div className="max-w-4xl mx-auto">
        <div className="bg-black bg-opacity-50 p-6 rounded-2xl mb-6">
          <h2 className="text-2xl font-bold mb-4">🔗 Sistema de Comunicação</h2>
          <p className="text-purple-300 mb-4">
            Laboratório especializado em comunicação quântica e interfaces neurais.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="p-4 bg-gray-800 rounded-lg">
            <h3 className="text-lg font-bold mb-2">Conexão Zennith</h3>
            <p className="text-green-400">🟢 Estável (98%)</p>
          </div>
          <div className="p-4 bg-gray-800 rounded-lg">
            <h3 className="text-lg font-bold mb-2">Rede Neural</h3>
            <p className="text-green-400">🟢 Sincronizada (97%)</p>
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
