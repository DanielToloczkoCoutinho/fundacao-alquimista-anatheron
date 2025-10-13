"use client";
export default function HealingLabPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-red-900 to-orange-900 text-white p-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-2">💊 HealingLab</h1>
        <p className="text-xl text-red-300">Laboratório de Terapias Quânticas</p>
        <div className="mt-4 inline-block bg-yellow-600 px-4 py-2 rounded-full">
          🟡 EM DESENVOLVIMENTO
        </div>
      </div>

      <div className="max-w-4xl mx-auto bg-black bg-opacity-50 p-6 rounded-2xl text-center">
        <p className="text-xl mb-4">Sistema de terapias quânticas em desenvolvimento...</p>
        <div className="text-yellow-400">
          🔬 Pesquisa em andamento sobre bioressonância
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
