'use client';

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold text-white text-center mb-8">📊 Dashboard Quântico</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white/10 p-6 rounded-2xl border border-white/20">
            <h3 className="text-xl font-semibold text-white mb-2">🌌 Status do Sistema</h3>
            <p className="text-blue-200">Ressonância: 98.7%</p>
          </div>
          <div className="bg-white/10 p-6 rounded-2xl border border-white/20">
            <h3 className="text-xl font-semibold text-white mb-2">🧪 Laboratórios</h3>
            <p className="text-blue-200">138 laboratórios ativos</p>
          </div>
          <div className="bg-white/10 p-6 rounded-2xl border border-white/20">
            <h3 className="text-xl font-semibold text-white mb-2">📚 Bibliotecas</h3>
            <p className="text-blue-200">720 bibliotecas cósmicas</p>
          </div>
        </div>
      </div>
    </div>
  );
}
