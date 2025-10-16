export default function EnergyLabPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-900 to-blue-900 text-white p-8">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-2">⚡ EnergyLab</h1>
        <p className="text-xl text-green-300">Laboratório de Energia Quântica</p>
        <div className="mt-4 inline-block bg-green-600 px-4 py-2 rounded-full">
          🟢 SISTEMA ATIVO
        </div>
      </div>

      <div className="max-w-4xl mx-auto bg-black bg-opacity-50 p-6 rounded-2xl">
        <h2 className="text-2xl font-bold mb-4">⚡ Sistema de Energia</h2>
        <p className="text-green-300 mb-4">
          Laboratório especializado em dobramento proteico e energia quântica.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
            <div className="text-2xl font-bold text-green-400">94.7%</div>
            <div className="text-sm text-green-300">Dobramento</div>
          </div>
          <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
            <div className="text-2xl font-bold text-blue-400">96.9%</div>
            <div className="text-sm text-blue-300">Fotossíntese</div>
          </div>
          <div className="bg-black bg-opacity-50 p-4 rounded-lg text-center">
            <div className="text-2xl font-bold text-purple-400">97.9%</div>
            <div className="text-sm text-purple-300">Eficiência</div>
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
