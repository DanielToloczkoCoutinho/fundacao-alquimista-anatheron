'use client';

export default function LaboratoriosPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold text-white text-center mb-8">🧪 Laboratórios Multidimensionais</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white/10 p-6 rounded-2xl border border-white/20">
            <h3 className="text-xl font-semibold text-white mb-2">🧪 Laboratório Quântico</h3>
            <p className="text-blue-200 mb-4">Pesquisa avançada em física quântica multidimensional</p>
            <div className="text-sm text-green-400">Status: Ativo</div>
          </div>
          <div className="bg-white/10 p-6 rounded-2xl border border-white/20">
            <h3 className="text-xl font-semibold text-white mb-2">💊 Laboratório de Cura</h3>
            <p className="text-blue-200 mb-4">Tecnologias de regeneração e rejuvenescimento</p>
            <div className="text-sm text-green-400">Status: Ativo</div>
          </div>
        </div>
      </div>
    </div>
  );
}
